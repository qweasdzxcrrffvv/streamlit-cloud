import streamlit as st
from modules import m_streamlit_enhance as stE

## =============================================================================    

t = [
    'Tx: 原发肿瘤不能评估',
    'T0: 无肿瘤证据',
    'Tis: 原位癌（DCIS 或 乳头 Paget 病）',
    'T1: 肿瘤最大径 ≤ 20mm',
    'T1mi: 肿瘤最大径 ≤ 1mm',
    'T1a: 肿瘤最大径 ≤ 5mm',
    'T1b: 肿瘤最大径 ≤ 10mm',
    'T1c: 肿瘤最大径 ≤ 20mm',
    'T2: 肿瘤最大径 ≤ 50mm',
    'T3: 肿瘤最大径 > 50mm',
    'T4a: 侵犯胸壁（不包括单纯胸肌受累）',
    'T4b: 未达炎性乳癌标准的皮肤受累（溃疡/卫星结节/水肿/橘皮样变）',
    'T4c: 同时存在 T4a 和 T4b ',
    'T4d: 炎性乳癌',
]

n = [
    'Nx: 区域淋巴结转移情况无法评估',
    'cN0: 无局部淋巴结转移',
    'cN1: 同侧 I、II 水平腋窝淋巴结，可活动',
    'cN2a: 同侧 I、II 水平腋窝淋巴结，固定/融合',
    'cN2b: 无腋窝淋巴结转移，但同侧内乳淋巴结转移',
    'cN3a: 同侧锁骨下淋巴结转移',
    'cN3b: 同侧内乳淋巴结和腋窝淋巴结转移',
    'cN3c: 同侧锁骨上淋巴结转移',
    'pN1a: 1-3 枚腋窝淋巴结宏转移',
    'pN1b: 同侧内乳前哨淋巴结转移',
    'pN1c: pN1a + pN1b',
    'pN2a: 4-9 枚腋窝淋巴结宏转移',
    'pN2b: 内乳淋巴结转移，不伴同侧腋窝淋巴结转移',
    'pN3a: 10 枚及以上腋窝淋巴结宏转移；或同侧锁骨下淋巴结转移',
    'pN3b: 内乳淋巴结转移伴 1-9 枚同侧腋窝淋巴结转移',
    'pN3c: 同侧锁骨上淋巴结转移',
]

m = [
    'M0: 无远处转移',
    'M1: 有远处转移'
]

## =============================================================================    

def list_to_html(lst, css_class="html_list"):
    output = ''
    for item in lst:
        output += f'<li>{item}</li>'
    output = f'<ul class={css_class}>' + output + '</ul>'
    return output

## =============================================================================    

con = st.expander('TNM Staging for Breast Cancer'.upper(), expanded=True)
with con:
    col1, col2, col3, col4 = st.columns(4)
    ts = col1.selectbox('T', options=['','x', 'is','0','1','1mi','1a','1b','1c','2','3','4','4a','4b','4c','4d'])
    ns = col2.selectbox('N', options=['','x','0','1','1a','1b','1c','2','2a','2b','3a','3b','3c'])
    ms = col3.selectbox('M', options=['','x','0','1'])

# --------------------------------------------------------------------------

stE.set_blank()
with st.expander('T', expanded=True):
    stE.set_html(list_to_html(t))
with st.expander('N', expanded=True):
    stE.set_html(list_to_html(n))
with st.expander('M', expanded=True):
    stE.set_html(list_to_html(m))

# --------------------------------------------------------------------------

if ms == '1':
    stage = 'Ⅳ'
elif ns.startswith('3'):
    stage = 'Ⅲc'
elif ts.startswith('4'):
    stage = 'Ⅲb'
elif ns.startswith('2') or (ts.startswith('3') and ns.startswith('1')):
    stage = 'Ⅲa'
elif (ts.startswith('2') and ns.startswith('1')) or (ts.startswith('3') and ns.startswith('0')):
    stage = 'Ⅱb'
elif (ts.startswith('0') and ns.startswith('1')) or (ts.startswith('1') and ns.startswith('1')) or (ts.startswith('2') and ns.startswith('0')):
    stage = 'Ⅱa'
elif (ts.startswith('0') and ns.startswith('1mi')) or (ts.startswith('1') and ns.startswith('1mi')):
    stage = 'Ⅰb'
elif (ts.startswith('1') and ns.startswith('0')):
    stage = 'Ⅰa'
elif (ts.startswith('is') and ns.startswith('0')):
    stage = '0'
else:
    stage = '/'

# --------------------------------------------------------------------------

with con:
    col4.text_input('Stage', value=stage, disabled=True)
    col1, col2 = st.columns(2)
    col1.text_input('TNM 分期', value = f'T{ts}N{ns}M{ms}, {stage} 期', disabled=True)
    col2.text_input('TNM Staging', value = f'T{ts}N{ns}M{ms}, Stage {stage}', disabled=True)

# --------------------------------------------------------------------------

stE.set_css_codes('''

    .html_list li {
        zoom:0.9;
        color:#888
    }
    
    .html_list {
        margin-bottom:10px
    }

''')

