"use strict";
/** Richard Stein project: independent local Git blob SHA-1 content verification for UTF-8 text, no network, signer, or wallet execution. */
function utf8EncodeManual(s) {
 const out=[];
 for(const ch of s) {
  const cp=ch.codePointAt(0);
  if(cp<0x80)out.push(cp);
  else if(cp<0x800)out.push(0xc0|(cp>>6),0x80|(cp&63));
  else if(cp<0x10000)out.push(0xe0|(cp>>12),0x80|((cp>>6)&63),0x80|(cp&63));
  else out.push(0xf0|(cp>>18),0x80|((cp>>12)&63),0x80|((cp>>6)&63),0x80|(cp&63));
 }
 return out;
}

function sha1PureJs(input) {
 const m=Array.from(input), originalLength=m.length;
 m.push(0x80);
 while(m.length%64!==56)m.push(0);
 let hi=Math.floor(originalLength*8/4294967296)>>>0,lo=(originalLength*8)>>>0;
 for(let s=24;s>=0;s-=8)m.push((hi>>>s)&255);
 for(let s=24;s>=0;s-=8)m.push((lo>>>s)&255);
 let h0=0x67452301,h1=0xefcdab89,h2=0x98badcfe,h3=0x10325476,h4=0xc3d2e1f0;
 const rot=(v,n)=>(v<<n)|(v>>>(32-n));
 for(let base=0;base<m.length;base+=64){
  const w=new Array(80);
  for(let i=0;i<16;i++)w[i]=((m[base+4*i]<<24)|(m[base+4*i+1]<<16)|(m[base+4*i+2]<<8)|m[base+4*i+3])>>>0;
  for(let i=16;i<80;i++)w[i]=rot(w[i-3]^w[i-8]^w[i-14]^w[i-16],1)>>>0;
  let a=h0,b=h1,c=h2,d=h3,e=h4;
  for(let i=0;i<80;i++){
   let f,k;
   if(i<20){f=(b&c)|(~b&d);k=0x5a827999}
   else if(i<40){f=b^c^d;k=0x6ed9eba1}
   else if(i<60){f=(b&c)|(b&d)|(c&d);k=0x8f1bbcdc}
   else{f=b^c^d;k=0xca62c1d6}
   const temp=(rot(a,5)+f+e+k+w[i])>>>0;
   e=d;d=c;c=rot(b,30)>>>0;b=a;a=temp;
  }
  h0=(h0+a)>>>0;h1=(h1+b)>>>0;h2=(h2+c)>>>0;h3=(h3+d)>>>0;h4=(h4+e)>>>0;
 }
 return [h0,h1,h2,h3,h4].map(v=>v.toString(16).padStart(8,"0")).join("");
}

function gitBlobSha1FromText(s){
 const body=utf8EncodeManual(s),header=utf8EncodeManual("blob "+body.length+"\0");
 return {sha:sha1PureJs(header.concat(body)),byte_length:body.length};
}

if(typeof module!=="undefined"&&module.exports)module.exports={utf8EncodeManual,sha1PureJs,gitBlobSha1FromText};
