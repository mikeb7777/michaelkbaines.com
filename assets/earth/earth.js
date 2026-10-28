/* Earth emerging from the dark. One full-screen WebGL2 quad: the globe is ray-traced per pixel,
   so it stays sharp at any size. Clouds ride on their own shell, turn at their own pace and cast shadows; relief comes from an elevation map. Textures: NASA Blue Marble oceans and clouds (public domain); land and night lights at 8K from
   Solar System Scope (CC BY 4.0, colour-matched and composited).
   Falls back to the static poster when WebGL2 is missing or motion is reduced. */
(function () {
  var host = document.querySelector('.space');
  if (!host) return;
  var cv = host.querySelector('canvas');
  var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var gl = cv.getContext('webgl2', { antialias: false, alpha: false, powerPreference: 'high-performance' });
  if (!gl) { host.classList.add('static'); return; }

  var base = cv.getAttribute('data-base') || 'assets/earth/';
  /* texture tier: 8K only on true desktop-class screens. Tablets/phones get 4K/2K, because
     iOS and iPadOS Safari cannot reliably decode the 33.6MP 8K JPEGs and silently fail. */
  var sLong = Math.max(screen.width, screen.height), sShort = Math.min(screen.width, screen.height);
  var px = sLong * (window.devicePixelRatio || 1);
  var maxTex = gl.getParameter(gl.MAX_TEXTURE_SIZE);
  var touch = (navigator.maxTouchPoints || 0) > 0;
  var iOS = /iP(hone|ad|od)/.test(navigator.userAgent) ||
            (navigator.platform === 'MacIntel' && (navigator.maxTouchPoints || 0) > 1);
  var mob = sShort < 600;
  var res = (mob || maxTex < 4096) ? '2k'
          : (!iOS && !touch && sShort >= 1100 && px >= 2600 && maxTex >= 8192) ? '8k'
          : '4k';
  /* if a tier's textures fail to decode, step down a tier rather than falling to the static poster */
  var CHAIN = res === '8k' ? ['8k', '4k', '2k'] : res === '4k' ? ['4k', '2k'] : ['2k'];

  var VS = '#version 300 es\nin vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
  var FS = [
    '#version 300 es',
    'precision highp float;',
    'uniform sampler2D uDay,uNight,uCloud,uSurf;',
    'uniform vec2 uRes;uniform vec3 uGeo;uniform float uSpin,uCloudSpin,uIntro,uTime,uDpr;uniform vec2 uTilt;',
    'out vec4 o;',
    'const float PI=3.14159265;',
    'float h21(vec2 p){p=fract(p*vec2(123.34,456.21));p+=dot(p,p+45.32);return fract(p.x*p.y);}',
    'mat3 rx(float a){float c=cos(a),s=sin(a);return mat3(1,0,0,0,c,s,0,-s,c);}',
    'mat3 ry(float a){float c=cos(a),s=sin(a);return mat3(c,0,-s,0,1,0,s,0,c);}',
    'mat3 rz(float a){float c=cos(a),s=sin(a);return mat3(c,s,0,-s,c,0,0,0,1);}',
    'vec4 tex(sampler2D t,vec2 uv,vec2 dx,vec2 dy){return textureGrad(t,uv,dx,dy);}',
    'vec2 wrapd(vec2 d){d.x-=floor(d.x+.5);return d;}',
    /* sparse stars and a few distant galaxies */
    'vec3 sky(vec2 f){',
    '  vec3 c=vec3(0.);',
    '  float s=7.*uDpr;vec2 g=floor(f/s);float h=h21(g);',
    '  if(h>.9982){vec2 q=(fract(f/s)-.5)*s;float b=h21(g+7.1);float r=length(q);',
    '    float tw=.75+.25*sin(uTime*(1.+b*2.)+h*40.);',
    '    c+=mix(vec3(.75,.85,1.),vec3(1.,.9,.75),b)*exp(-r*r/(.9*uDpr*uDpr))*(.35+1.4*b*b)*tw;}',
    '  vec2 u=f/uRes.y;',
    '  vec4 G[4];G[0]=vec4(.16,.78,.020,.6);G[1]=vec4(.42,.22,.013,-.9);G[2]=vec4(.07,.30,.009,.2);G[3]=vec4(.55,.88,.007,1.3);',
    '  for(int i=0;i<4;i++){vec2 d=u-G[i].xy*vec2(uRes.x/uRes.y,1.);float a=G[i].w;d=mat2(cos(a),-sin(a),sin(a),cos(a))*d;',
    '    d.y*=2.6;float r=length(d)/G[i].z;float arm=.5+.5*sin(atan(d.y,d.x)*2.-r*4.);',
    '    c+=vec3(.86,.90,.95)*(exp(-r*r*.9)*.16*(.6+.4*arm)+exp(-r*r*14.)*.35);}',
    '  return c;}',
    'float lum(vec3 c){return dot(c,vec3(.2126,.7152,.0722));}',
    'vec3 sat(vec3 c,float k){float l=lum(c);return max(vec3(0.),mix(vec3(l),c,k));}',
    /* cloud cover at a direction on the cloud shell, which turns on its own */
    'float cloudAt(vec3 d,mat3 Mc,vec2 dx,vec2 dy){vec3 w=Mc*d;vec2 uv=vec2(atan(w.x,w.z)/(2.*PI)+.5,.5-asin(clamp(w.y,-1.,1.))/PI);return smoothstep(.05,1.,tex(uCloud,uv,dx,dy).r);}',
    'void main(){',
    '  vec2 f=gl_FragCoord.xy;',
    '  vec2 p=(f-uGeo.xy)/uGeo.z;',
    '  float r2=dot(p,p),r=sqrt(r2);',
    '  float I=smoothstep(0.,1.,uIntro);',
    /* sun: starts behind the planet, swings round to light it from the upper left */
    '  float sa=mix(2.85,1.22,I);',
    '  vec3 L=normalize(vec3(-sin(sa),.32,cos(sa)));',
    '  vec3 col=sky(f)*smoothstep(.0,.6,uIntro);',
    '  mat3 M=ry(uSpin)*rx(uTilt.y)*rz(-.41+uTilt.x);',
    '  mat3 Mc=ry(uSpin+uCloudSpin)*rx(uTilt.y)*rz(-.41+uTilt.x);',
    '  const float RC=1.0065;',
    '  float px1=1./uGeo.z;',
    '  if(r<1.){',
    '    float z=sqrt(1.-r2);vec3 n=vec3(p,z);',
    '    vec3 w=M*n;',
    '    float lon=atan(w.x,w.z),lat=asin(clamp(w.y,-1.,1.));',
    '    vec2 uv=vec2(lon/(2.*PI)+.5,.5-lat/PI);',
    '    vec2 dx=wrapd(dFdx(uv)),dy=wrapd(dFdy(uv));',
    /* day colour with an unsharp mask so coastlines and continents read crisp, not muddy */
    '    vec2 dt=vec2(1.)/vec2(textureSize(uDay,0));',
    '    vec3 d0=tex(uDay,uv,dx,dy).rgb;',
    '    vec3 dR=tex(uDay,uv+vec2(dt.x,0.),dx,dy).rgb,dL=tex(uDay,uv-vec2(dt.x,0.),dx,dy).rgb;',
    '    vec3 dU=tex(uDay,uv-vec2(0.,dt.y),dx,dy).rgb,dD=tex(uDay,uv+vec2(0.,dt.y),dx,dy).rgb;',
    '    d0+=(d0*4.-dR-dL-dU-dD)*.17;',
    '    vec3 day=pow(max(d0,0.),vec3(2.2));',
    '    vec3 ngt=pow(tex(uNight,uv,dx,dy).rgb,vec3(2.2));',
    '    vec4 sf=tex(uSurf,uv,dx,dy);float water=smoothstep(.35,.65,sf.r);',
    /* relief: elevation map for mountains, fine colour detail from the land map */
    '    vec2 ts=vec2(1./2048.,1./1024.);',
    '    float he=tex(uSurf,uv+vec2(ts.x,0.),dx,dy).g-tex(uSurf,uv-vec2(ts.x,0.),dx,dy).g;',
    '    float hn=tex(uSurf,uv-vec2(0.,ts.y),dx,dy).g-tex(uSurf,uv+vec2(0.,ts.y),dx,dy).g;',
    '    float fe=lum(dR)-lum(dL),fn=lum(dU)-lum(dD);',
    '    float cl0=cos(lat);vec3 E=vec3(cos(lon),0.,-sin(lon)),N=vec3(-sin(lon)*sin(lat),cl0,-cos(lon)*sin(lat));',
    '    float land=1.-water;',
    '    vec3 nw=normalize(w-(E*(he*10.+fe*3.2)+N*(hn*10.+fn*3.2))*land);',
    '    vec3 Lw=M*L;',
    '    float d=dot(n,L);',
    '    float dr=mix(d,dot(nw,Lw),.85);',
    '    float lit=smoothstep(-.06,.28,d);',
    /* clouds sit on a shell just above the ground and cast a soft shadow away from the sun */
    '    float s=-d+sqrt(d*d+RC*RC-1.);',
    '    float shd=cloudAt(normalize(n+L*s*1.6),Mc,dx,dy);',
    '    float shadow=1.-.55*shd*smoothstep(-.1,.2,d);',
    '    vec3 V=vec3(0,0,1);vec3 H=normalize(L+V);',
    '    float nh=max(dot(n,H),0.);',
    '    float spec=(pow(nh,260.)*.75+pow(nh,36.)*.035)*water;',
    '    vec3 surf=day*max(dr,0.)*1.3*shadow+vec3(1.,.93,.8)*spec*lit*shadow;',
    '    float nightMask=(1.-smoothstep(-.18,.06,d));',
    '    float nl=dot(ngt,vec3(.3,.59,.11));surf+=vec3(1.,.72,.38)*smoothstep(.03,.5,nl)*nl*nightMask*2.2*(1.-.8*cloudAt(n,Mc,dx,dy));',
    '    float rim=pow(1.-z,2.6);',
    '    surf=surf*(1.-rim*.35)+vec3(.30,.55,1.)*rim*smoothstep(-.25,.45,d)*1.1;',
    '    float edge=smoothstep(1.,1.-1.5*px1,r);',
    '    col=mix(col,surf,edge);',
    '  }',
    /* the cloud layer: its own rotation, lit with relief taken from its thickness */
    '  if(r<RC){',
    '    float zc=sqrt(RC*RC-r2);vec3 c=vec3(p,zc)/RC;',
    '    vec3 w=Mc*c;',
    '    float lon=atan(w.x,w.z),lat=asin(clamp(w.y,-1.,1.));',
    '    vec2 uv=vec2(lon/(2.*PI)+.5,.5-lat/PI);',
    '    vec2 dx=wrapd(dFdx(uv)),dy=wrapd(dFdy(uv));',
    '    float cl=smoothstep(.05,1.,tex(uCloud,uv,dx,dy).r);',
    '    vec2 ct=vec2(1.)/vec2(textureSize(uCloud,0));',
    '    float ce=tex(uCloud,uv+vec2(ct.x,0.),dx,dy).r-tex(uCloud,uv-vec2(ct.x,0.),dx,dy).r;',
    '    float cn=tex(uCloud,uv-vec2(0.,ct.y),dx,dy).r-tex(uCloud,uv+vec2(0.,ct.y),dx,dy).r;',
    '    vec3 E=vec3(cos(lon),0.,-sin(lon)),N=vec3(-sin(lon)*sin(lat),cos(lat),-cos(lon)*sin(lat));',
    '    vec3 nw=normalize(w-(E*ce+N*cn)*3.);',
    '    float d=dot(c,L),dc=mix(d,dot(nw,Mc*L),.45)*smoothstep(-.08,.22,d);',
    '    vec3 ccol=vec3(1.,.985,.96)*max(dc,0.)*1.08+vec3(.05,.08,.14)*smoothstep(-.2,.3,d);',
    '    ccol*=mix(.82,1.,smoothstep(.2,.9,cl));',
    '    float a=cl*.95*smoothstep(RC,RC-1.5*px1,r);',
    '    if(r>1.)a*=.85;',
    '    col=mix(col,ccol,a);',
    '  }',
    /* atmosphere glow outside the limb, only on the sunlit side */
    '  if(r>.985){',
    '    vec3 n=normalize(vec3(p,0.));float dl=dot(n,L);',
    '    float g=exp(-(r-1.)*uGeo.z/(9.*uDpr))*smoothstep(-.35,.55,dl);',
    '    float g2=exp(-(r-1.)*uGeo.z/(45.*uDpr))*smoothstep(-.2,.8,dl)*.08;',
    '    col+=vec3(.35,.62,1.)*(g*.75+g2)*smoothstep(.985,1.,r);',
    '  }',
    '  col*=smoothstep(0.,.35,uIntro)*.25+.75*I+.0;',
    /* commercial grade: filmic shoulder, richer colour, a touch more contrast */
    '  col=col/(1.+col*.32);',
    '  col=sat(col,1.22);',
    '  col=pow(col,vec3(1./2.2));',
    '  col=mix(col,col*col*(3.-2.*col),.22);',
    '  col+=(h21(f+uTime)-.5)/255.;',
    '  o=vec4(col,1.);',
    '}'
  ].join('\n');

  function sh(t, s) { var x = gl.createShader(t); gl.shaderSource(x, s); gl.compileShader(x); if (!gl.getShaderParameter(x, gl.COMPILE_STATUS)) { console.warn(gl.getShaderInfoLog(x)); return null; } return x; }
  var vs = sh(gl.VERTEX_SHADER, VS), fs = sh(gl.FRAGMENT_SHADER, FS);
  if (!vs || !fs) { host.classList.add('static'); return; }
  var pr = gl.createProgram(); gl.attachShader(pr, vs); gl.attachShader(pr, fs); gl.linkProgram(pr); gl.useProgram(pr);
  var b = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, b);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
  var loc = gl.getAttribLocation(pr, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
  var U = {}; ['uDay', 'uNight', 'uCloud', 'uSurf', 'uRes', 'uGeo', 'uSpin', 'uCloudSpin', 'uIntro', 'uTime', 'uDpr', 'uTilt'].forEach(function (k) { U[k] = gl.getUniformLocation(pr, k); });

  var aniso = gl.getExtension('EXT_texture_filter_anisotropic');
  function load(unit, name, src) {
    return new Promise(function (ok, bad) {
      var im = new Image(); im.decoding = 'async';
      im.onload = function () {
        var t = gl.createTexture(); gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t);
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, im);
        gl.generateMipmap(gl.TEXTURE_2D);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        if (aniso) gl.texParameterf(gl.TEXTURE_2D, aniso.TEXTURE_MAX_ANISOTROPY_EXT, 8);
        gl.uniform1i(U[name], unit); ok();
      };
      im.onerror = bad; im.src = base + src;
    });
  }

  var W = 0, H = 0, dpr = 1;
  function geo() {
    /* the planet sits to the right, partly beyond the edge, as if drifting in */
    var mob = W / dpr < 760;
    if (mob) return [W * 0.64, Math.min(H * 0.30, W * 0.78), W * 0.62];
    return [W * 0.84, H * 0.50, Math.min(H * 0.54, W * 0.36)];
  }
  function size() {
    dpr = Math.min(2, window.devicePixelRatio || 1);
    var r = cv.getBoundingClientRect();
    W = Math.round(r.width * dpr); H = Math.round(r.height * dpr);
    if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
    gl.viewport(0, 0, W, H);
  }

  var t0 = 0, introDur = 4.2, spin0 = 2.2, tx = 0, ty = 0, cx = 0, cy = 0, run = true, ready = false;
  function frame(ts) {
    if (!t0) t0 = ts;
    var t = (ts - t0) / 1000;
    var intro = still ? 1 : Math.min(1, t / introDur);
    cx += (tx - cx) * 0.04; cy += (ty - cy) * 0.04;
    var g = geo();
    gl.uniform2f(U.uRes, W, H);
    gl.uniform3f(U.uGeo, g[0], H - g[1], g[2]);
    gl.uniform1f(U.uSpin, spin0 + (still ? 0 : t * 0.018));
    gl.uniform1f(U.uCloudSpin, 0.35 + (still ? 0 : t * 0.0075));
    gl.uniform1f(U.uIntro, intro);
    gl.uniform1f(U.uTime, still ? 0 : t);
    gl.uniform1f(U.uDpr, dpr);
    gl.uniform2f(U.uTilt, cx * 0.06, cy * 0.05);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    if (!ready) { ready = true; host.classList.add('live'); }
    if (run && !still) requestAnimationFrame(frame);
  }
  size();
  window.addEventListener('resize', function () { size(); if (still) requestAnimationFrame(frame); });
  host.addEventListener('pointermove', function (e) {
    var r = host.getBoundingClientRect();
    tx = (e.clientX - r.left) / r.width - 0.5; ty = (e.clientY - r.top) / r.height - 0.5;
  });
  new IntersectionObserver(function (es) {
    var vis = es[0].isIntersecting && !document.hidden;
    if (vis && !run) { run = true; requestAnimationFrame(frame); } else if (!vis) run = false;
  }).observe(host);
  document.addEventListener('visibilitychange', function () { if (!document.hidden && !run) { run = true; requestAnimationFrame(frame); } });

  function boot(i) {
    var r = CHAIN[i], cr = r === '8k' ? '4k' : r;
    Promise.all([
      load(0, 'uDay', 'day-' + r + '.jpg'),
      load(1, 'uNight', 'night-' + r + '.jpg'),
      load(2, 'uCloud', 'clouds-' + cr + '.jpg'),
      load(3, 'uSurf', 'surface-2k.png')
    ]).then(function () { t0 = 0; requestAnimationFrame(frame); })
      .catch(function () { if (i + 1 < CHAIN.length) boot(i + 1); else host.classList.add('static'); });
  }
  boot(0);
})();
