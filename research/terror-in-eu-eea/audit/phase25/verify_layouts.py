"""Check SVG accessibility metadata and rendered text extents with Inkscape."""
import csv
import subprocess
from tempfile import TemporaryDirectory
from pathlib import Path
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parent / 'figures'
ns = '{http://www.w3.org/2000/svg}'
for f in sorted(root.rglob('*.svg')):
    svg = ET.parse(f).getroot()
    width, height = (int(svg.attrib[k]) for k in ('width', 'height'))
    text = list(svg.iter(ns + 'text'))
    for i, e in enumerate(text):
        e.set('id', f't{i}')
    with TemporaryDirectory() as temp:
        probe = Path(temp) / 'probe.svg'
        ET.ElementTree(svg).write(probe, encoding='utf-8')
        query = subprocess.check_output(['inkscape', str(probe), '--query-all'],
                                        text=True, stderr=subprocess.DEVNULL)
    bounds = {r[0]: list(map(float, r[1:])) for r in csv.reader(query.splitlines())}
    assert svg.findtext(ns+'title') and svg.findtext(ns+'desc') and svg.attrib['role']=='img'
    for i, el in enumerate(text):
        x,y,w,h = bounds[f't{i}']
        assert x>=0 and y>=0 and x+w<=width and y+h<=height, (f,el.text,x,y,w,h)
        if f.parent.name == 'mobile' and el.attrib['x']=='18':
            assert x+w<=172,(f,el.text,x+w)
        if f.parent.name == 'mobile':
            assert int(el.attrib['font-size'])>=13
    print('PASS', f)
