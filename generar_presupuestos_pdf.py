import sys,io,json
sys.path.insert(0,'/tmp/claude-0/-home-user-Claude/2f56e824-52b2-5380-ba87-4345eb1fdd2d/scratchpad/build')
from decimal import Decimal as D
from model8 import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, white, black
from pypdf import PdfReader, PdfWriter
import copy
pdfmetrics.registerFont(TTFont('DJ','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DJB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
TPL='/tmp/claude-0/-home-user-Claude/2f56e824-52b2-5380-ba87-4345eb1fdd2d/scratchpad/pdf/tpl.pdf'
H=842
GR=Color(204/255,204/255,204/255); DK=Color(46/255,47/255,45/255); FG=Color(0.4,0.4,0.4)
def es(x): return f"{float(x):,.2f}".replace(",","X").replace(".",",").replace("X",".")
def y(top,size): return H-(top+0.928*size)           # baseline desde 'yMin' de pdftotext
def white_rect(c,x0,t0,x1,t1): c.setFillColor(white); c.setStrokeColor(white); c.rect(x0,H-t1,x1-x0,t1-t0,fill=1,stroke=0)
def txt(c,x,top,s,size=8,bold=False,color=black,align='l',maxw=None):
    f='DJB' if bold else 'DJ'
    if maxw:
        while pdfmetrics.stringWidth(s,f,size)>maxw and size>5.5: size-=0.25
    c.setFont(f,size); c.setFillColor(color)
    {'l':c.drawString,'r':c.drawRightString,'c':c.drawCentredString}[align](x,y(top,size),s)
def wrap(s,f,size,maxw):
    out=[];line=''
    for w in s.split(' '):
        t=(line+' '+w).strip()
        if pdfmetrics.stringWidth(t,f,size)<=maxw: line=t
        else: out.append(line); line=w
    if line: out.append(line)
    return out
NAMES={'trydan':"2 cargadores V2C Trydan Pro monofásicos 7,4 kW",'ekey':"Llaveros RFID 13,56 MHz (MIFARE), 3 uds",'cable':"Cable RZ1-K (AS) 3G10 mm², 2 líneas de 32 A (m)",
'tubo':"Tubo y fijaciones, líneas de fuerza (m)",'c40':"Magnetotérmico 2P C40 curva C",'diff40':"Diferencial 2P 40 A 30 mA tipo A superinm.",
'spd':"Protector sobretensiones perm. y transitorias",'iga':"Sustitución IGA por magnetotérmico 2P 63 A",'diffs':"Sustitución diferenciales cuadro vivienda",
'aux':"Material auxiliar y señalización",'utp':"Cable UTP Cat6 comunicaciones (m)",'tubocom':"Canalización comunicaciones aparte (m)",
'garcable':"Línea 3G2,5 y canalización toma garaje (m)",'garprot':"Toma garaje: C10, dif. 30 mA y base con llave",
'mo':"Mano de obra instalación y puesta en marcha (h)",'cie1':"Memoria técnica y CIE instalación de recarga",'cie2':"CIE vivienda 14,49 kW y gestión potencia P2"}
REFS={k:f"PRO{90+i:05d}" for i,k in enumerate(['trydan','ekey','cable','tubo','c40','diff40','spd','iga','diffs','aux','utp','tubocom','garcable','garprot','mo','cie1','cie2'])}
def notes(opt,cie_incl):
    base=[
 "Presupuesto sujeto a visita técnica. Los metros, los diferenciales a sustituir y las horas se ajustan a precio unitario tras la visita; la mano de obra se factura a 40 € + IVA por hora. Precios sin IVA; IVA 21 % en el total. Validez: 15 días."]
    if opt=='A':
        base+=["Los cargadores los compra el cliente. Requisitos del equipo: modo 3, monofásico 230 V, 32 A (7,4 kW) por toma, cable Type 2 fijo de 5 m, lector RFID y puerto Ethernet, control dinámico de potencia con medidor y pinza y balanceo entre dos cargadores, sin MID, IP54 o superior, ficha técnica y declaración CE. El cliente envía el enlace del modelo antes de comprar y PAV GROUP confirma por escrito en 24 horas si cumple.",
 "Los equipos deben estar en obra al menos 5 días laborables antes de la fecha de instalación y como máximo el 4/12/2026. PAV GROUP no responde del retraso en la entrega ni de equipos defectuosos o no conformes. Garantía de los equipos: la del vendedor ante el cliente (legal de 3 años, TRLGDCU, art. 120). Garantía de la instalación de PAV GROUP: 2 años.",
 "Forma de pago (a cuenta): 30 % al aceptar, 50 % al terminar la instalación, 20 % al entregar los CIE registrados. Los pagos a cuenta son devolvibles si el cliente ejerce su derecho legal de desistimiento de 14 días (TRLGDCU, arts. 102 y ss.)."]
    else:
        base+=["Plazo: la instalación y su puesta en servicio se planifican antes del 31/12/2026, siempre que los equipos estén en obra como máximo el 4/12/2026. Si los equipos no están en obra el 15/12/2026, el cliente puede desistir con devolución íntegra de lo pagado.",
 "Forma de pago (a cuenta): 40 % al aceptar, 40 % al terminar la instalación, 20 % al entregar los CIE registrados. Los pagos a cuenta son devolvibles si el cliente ejerce su derecho legal de desistimiento de 14 días (TRLGDCU, arts. 102 y ss.).",
 "Garantía: equipos, la legal de 3 años desde la entrega (TRLGDCU, art. 120) y la comercial del fabricante; instalación, 2 años."]
    base+=[f"CIE de la vivienda: incluido en el precio total. Si el boletín actual ya admite 14,49 kW, se descuenta íntegramente ({cie_incl} € con IVA).",
 "Los cargadores V2C Trydan Pro no incorporan la norma EN ISO 15118-20 (comunicado del representante de V2C el 12/11/2026). Por eso la instalación debe quedar terminada y en servicio en 2026; una sustitución o renovación posterior de los cargadores deberá cumplir esa norma (Reglamento Delegado (UE) 2025/656, anexo II, punto 2.1.3)." if opt=='B' else
 "Los cargadores V2C Trydan Pro no incorporan la norma EN ISO 15118-20 (comunicado del representante de V2C el 12/11/2026). La instalación debe quedar terminada y en servicio en 2026; una sustitución o renovación posterior de los cargadores deberá cumplir esa norma (Reglamento Delegado (UE) 2025/656, anexo II, punto 2.1.3). Si el cliente compra otro modelo, el estado de la ISO lo declara el fabricante o el vendedor.",
 "No incluye: obra civil y acabados; derivación individual, LGA o centralización del edificio si no admiten 14,49 kW; iluminación del garaje si no alcanza 50 lux a nivel de suelo (ITC-BT-52, apartado 5); comunicación a la comunidad (LPH, art. 17.5); tasas administrativas, derechos de acceso o extensión y costes de e-distribución (los factura la comercializadora); configuración del router y de la red del cliente; detector de fugas DC (opcional V2C); ayudas."]
    return base

LOGO='/tmp/claude-0/-home-user-Claude/2f56e824-52b2-5380-ba87-4345eb1fdd2d/scratchpad/pdf/logo_opaco.png'
def logo_patch(c):
    white_rect(c,29,11,252,88.5)
    c.drawImage(LOGO,30,H-88,width=220,height=76)
def build_pdf(opt,num,subtitle,out,fecha='12/11/2026'):
    keys=[r for r in R if not (opt=='A' and r[0]=='trydan')]
    L=build(keys); S,C,I,T,M=totals(L)
    cie_incl=es(L[-1]['imp']*D('1.21'))
    buf=io.BytesIO(); c=canvas.Canvas(buf,pagesize=(595,842))
    # ---------- página 1
    logo_patch(c)
    white_rect(c,60,106,540,124); txt(c,297.5,109.7,subtitle,10,align='c',maxw=470)
    white_rect(c,18,147,200,170); txt(c,20,149.4,"Número:",8); txt(c,57.2,149.4,num,8,True); txt(c,20,159.4,"Fecha:",8); txt(c,49.1,159.4,fecha,8,True)
    white_rect(c,313,147,565,200)
    for t,(s,b) in zip((149.4,159.4,169.4,179.4,189.4),(("Anastasia (Sotogrande)",True),("NIF/NIE: [completar]",False),("[Dirección], Sotogrande, Cádiz, España",False),("España",False),("Telf.: [completar]",False))): txt(c,315,t,s,8,b)
    white_rect(c,18,224,580,626)
    top=227.4
    for i,l in enumerate(L):
        k=l['key']; yt=top+16*i
        txt(c,20,yt,REFS[k],8); txt(c,91,yt+0.1,NAMES[k],9,maxw=250)
        txt(c,380,yt,es(l['up']),8,align='r'); txt(c,420,yt,"0,00%",8,align='r'); txt(c,460,yt,es(l['q']),8,align='r'); txt(c,515,yt,es(l['imp']),8,align='r')
        txt(c,575,yt,"IVA 21,00%",8,align='r')
        c.setStrokeColor(GR); c.setLineWidth(0.5); c.line(20,H-(yt+11.6),574.5,H-(yt+11.6))
    white_rect(c,380,626,580,682)
    txt(c,387,631.4,"BASE",8,True,DK); txt(c,567.4,631.4,es(S),8,align='r'); txt(c,575,631.4,"€",8,align='r')
    c.setStrokeColor(GR); c.setLineWidth(1); c.line(387,H-641,573.5,H-641)
    txt(c,387,648.1,es(S),7); txt(c,459,648.1,"IVA 21,00%",7); txt(c,573,648.1,es(I),7,align='r')
    c.line(387,H-657,573.5,H-657)
    txt(c,387,664.4,"TOTAL",9,True,DK); txt(c,564.6,664.3,es(T),9,True,align='r'); txt(c,574,664.3,"€",9,True,align='r')
    white_rect(c,495,815,580,835); txt(c,576,817.5,f"{num} ({fecha})",6,color=FG,align='r'); txt(c,576,825.2,"1 / 2",7,color=FG,align='r')
    c.showPage()
    # ---------- página 2: condiciones
    logo_patch(c)
    white_rect(c,60,106,540,124); txt(c,297.5,109.7,"Condiciones y notas del presupuesto "+num,10,align='c')
    white_rect(c,18,126,580,770)
    txt(c,20,134.4,"CONDICIONES Y NOTAS",8,True,DK); c.setStrokeColor(GR); c.setLineWidth(1); c.line(20,H-144.5,574.5,H-144.5)
    yy=156
    for p in notes(opt,cie_incl):
        for ln in wrap(p,'DJ',8,552):
            txt(c,20,yy,ln,8); yy+=11
        yy+=5
    txt(c,20,yy+4,"Cantidades a confirmar en visita técnica: metros de línea y tubo, metros de UTP y número de diferenciales del cuadro. Referencias provisionales.",7,color=FG)
    white_rect(c,495,815,580,835); txt(c,576,817.5,f"{num} ({fecha})",6,color=FG,align='r'); txt(c,576,825.2,"2 / 2",7,color=FG,align='r')
    c.showPage(); c.save(); buf.seek(0)
    ov=PdfReader(buf); w=PdfWriter()
    for i in range(2):
        pg=PdfReader(TPL).pages[0]; pg.merge_page(ov.pages[i]); w.add_page(pg)
    w.add_metadata({'/Title':num+' '+subtitle,'/Author':'PAV GROUP'})
    with open(out,'wb') as f: w.write(f)
    return S,I,T,len(L)
O='/home/user/Claude/'
print(build_pdf('A','PRV00041',"Instalación de 2 puntos de recarga VE con balanceo (equipos del cliente)",O+'PRESUPUESTODEVENTA-00041-Opcion_A_Instalacion.pdf'))
print(build_pdf('B','PRV00042',"Instalación de 2 puntos de recarga VE con balanceo (llave en mano)",O+'PRESUPUESTODEVENTA-00042-Opcion_B_Llave_en_mano.pdf'))
