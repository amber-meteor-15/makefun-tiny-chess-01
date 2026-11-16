import json,os,urllib.request as U
E=os.getenv("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900,0]
S="PPPPPPPPSUUKKUUSSNUXXUNSPPU]]UPPSSZbbZSSUU]dd]UUZZbiibZZPPPPPPPP","7AFFFFA7AKPSSPKAFSXZZXSFFPZ]]ZPFFSX]]XSFFPUZZUPFAKPSSPKA7AFFFFA7","Z_UPPU_ZZZPKKPZZKFFFFFFKFAA<<AAFA<<77<<AA<<77<<AA<<77<<AA<<77<<A"
T=[[ord(c)*2-160 for c in s]for s in S]
T[2:2]=[T[1]]*3
D=(1,16,17,15,-1,-16,-17,-15)
G=[(31,33,14,18,-31,-33,-14,-18),(17,15,-17,-15),(1,16,-1,-16),D,D]
C={0:13,7:14,4:12,112:7,119:11,116:3}
UN=[];NB=3e4;MV={}
X=Exception
def sf(F):
 global B,sd,ct
 B=[0]*128;P=F.split();s=112
 for ch in P[0]:
  if ch=='/':s-=24
  elif ch<'9':s+=int(ch)
  else:
   p='?pnbrqk'.index(ch.lower())
   if ch>'Z':p=-p
   B[s]=p;s+=1
 sd=2*(P[1]=='w')-1
 ct=sum(v for c,v in zip('KQkq',(1,2,4,8))if c in P[2])
def at(s,w):
 u=2*w-1
 for d in(-15*u,-17*u):
  t=s+d
  if not t&136 and B[t]==u:return 1
 for D2,y,z in((G[0],2,0),(G[4],6,0),(G[1],3,1),(G[2],4,1)):
  for d in D2:
   t=s
   while 1:
    t+=d
    if t&136:break
    p=B[t]
    if p:
     if p==y*u or(z and p==5*u):return 1
     break
    if not z:break
 return 0
def L():return at(B.index(-6*sd),sd>0)
def gn(co=0):
 ms=[];A=ms.append
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or p*sd<0:continue
  a=abs(p)
  if a==1:
   d=16*sd
   for t,cp in((s+d,0),(s+d-1,1),(s+d+1,1)):
    if t&136:continue
    q=B[t]
    if cp:
     if not q or q*sd>0:continue
    elif q:continue
    if t>>4 in(0,7):
     for pr in(5,2,4,3):A(s|t<<7|pr<<14)
    elif cp or not co:
     A(s|t<<7)
     if not cp and s>>4==1+(sd<0)*5 and not B[s+2*d]:A(s|(s+2*d)<<7)
  else:
   for d in G[a-2]:
    t=s
    while 1:
     t+=d
     if t&136:break
     q=B[t]
     if not q:
      if not co:A(s|t<<7)
     else:
      if q*sd<0:A(s|t<<7)
      break
     if a in(2,6):break
 if not co:
  for b,f,em,ak,t in((1,4,(5,6),(4,5,6),6),(2,4,(1,2,3),(2,3,4),2),(4,116,(117,118),(116,117,118),118),(8,116,(113,114,115),(114,115,116),114)):
   if ct&b and not any(B[x]for x in em)and not any(at(x,sd<0)for x in ak):A(f|t<<7)
 return ms
def mk(m):
 global sd,ct
 f=m&127;t=m>>7&127;p=B[f];c=B[t]
 UN.append((m,c,ct))
 B[f]=0;B[t]=(m>>14)*sd if m>>14 else p
 if abs(p)==6 and abs(t-f)==2:
  g=1 if t>f else-1;rt=f+g;rf=f+(3+(g<0))*g;B[rt]=B[rf];B[rf]=0
 ct&=C.get(f,15)&C.get(t,15)
 sd=-sd
def um():
 global sd,ct
 m,c,ct=UN.pop()
 sd=-sd;f=m&127;t=m>>7&127;p=B[t]
 if abs(p)==6 and abs(t-f)==2:
  g=1 if t>f else-1;rt=f+g;rf=f+(3+(g<0))*g;B[rf]=B[rt];B[rt]=0
 B[f]=sd if m>>14 else p;B[t]=c
def EV():
 s=0
 for i,p in enumerate(B):
  if p:
   a=abs(p)
   if a!=6:s+=(V[a]+T[a-1][((i>>4)*8+(i&7))^(56*(p<0))])*(p//a)
 i=B.index(6);j=B.index(-6)
 return s+T[5][(i>>4)*8+(i&7)]-T[5][((j>>4)*8+(j&7))^56]
def od(ms,tm):
 def k2(m):
  return(m==tm)*1e7+((V[abs(c)]*16-V[abs(B[m&127])])if(c:=B[m>>7&127])else 0)
 return sorted(ms,key=k2,reverse=True)
def sr(d,a,b,p):
 global nd
 nd+=1
 if nd>NB:raise X
 if d<1:
  st=EV()*sd
  if at(B.index(6*sd),sd<0):return sr(1,a,b,p)
  if st>=b:return b
  if st>a:a=st
  for m in od(gn(1),0):
   mk(m)
   if L():um();continue
   s=-sr(0,-b,-a,p+1);um()
   if s>a:a=s
   if a>=b:break
  return a
 bs=-1e9;bmv=0
 for m in od(gn(),MV.get(0)if p==0 else 0):
  mk(m)
  if L():um();continue
  s=-sr(d-1,-b,-a,p+1);um()
  if s>bs:bs=s;bmv=m
  if s>a:a=s
  if a>=b:break
 if bs==-1e9:return-100000+p if at(B.index(6*sd),sd<0)else 0
 MV[p]=bmv
 return bs
def uc(m):
 f=m&127;t=m>>7&127;p=m>>14
 return bytes((97+(f&7),49+(f>>4),97+(t&7),49+(t>>4))).decode()+('nbrq'[p-2]if p else'')
def bm():
 global nd
 ms=[]
 for m in gn():
  mk(m)
  if not L():ms.append(m)
  um()
 b=ms[0];nd=0;d=1
 while d<65:
  try:
   s=sr(d,-1e9,1e9,0)
   b=MV[0]
  except X:break
  d+=1
 return b
J=lambda p,b:json.load(U.urlopen(U.Request(E+p,json.dumps(b).encode(),{'content-type':'application/json'})))
while 1:
 g=J('/game',{})
 if g['status']=='done':break
 while g['status']=='your_move':
  try:
   sf(g['fen']);u=uc(bm())
   if u not in g['legal_moves']:raise 0
  except Exception:u=g['legal_moves'][0]
  g=J('/move',{'game':g['game'],'move':u})
