with st.expander('基本信息', expanded=True):
        col1, col2, col3, col4 =st.columns(4)
        height = col1.text_input('身高 (cm)')
        weight = col2.text_input('体重 (kg)')
        if height != '' and weight != '':
            bsa = f_bsa.run(height, weight)
        else:
            bsa = ''
        col3.text_input('体表面积',value=bsa, disabled=True)
        is_calc_auc = col4.selectbox('计算 AUC',options=['','否','是'], index=1)

    # --------------------------------------------------------------------------

        if is_calc_auc == '是':
            col1, col2, col3, col4, col5 =st.columns((3,3,3,4,5))
            sex = col1.selectbox('性别',options=['女','男'], index=0)
            age = col2.selectbox('年龄 (岁)', options=O.range(0,100))
            age = int(age) if age not in ['','/'] else 0
            
            # 血清肌酐、肌酐清除率
            scr = col3.selectbox(label='血清肌酐', options=O.range(0,1000))
            scr_unit = col4.selectbox(label='血清肌酐单位',key='血清肌酐单位', options=['μmol/L','mg/dl'])

            if scr not in ['','/'] and age not in ['','/']:
                scr = int(scr) if scr not in ['','/'] else 0
                if (scr>125 and scr_unit =='μmol/L') or (scr>1.41 and scr_unit =='mg/dl'):
                    st.caption('患者肾功能严重不全，请结合实际情况调整药物剂量。')

                if scr not in ['','/']:
                    ccr = f_creatinine_clearance.run (
                                        sex,
                                        age,
                                        weight.replace(' kg',''),
                                        scr,
                                        scr_unit
                                    )
                    col5.text_input(label='肌酐清除率',
                                    key='肌酐清除率', 
                                    disabled=True,
                                    value = str(ccr) + ' mL/min')
                else:
                    col5.text_input(label='肌酐清除率', key='肌酐清除率', disabled=True)

    # --------------------------------------------------------------------------
    
    with st.expander('药物剂量', expanded=True):
        drugs = st.multiselect('药物', key='drugs', options=O.chemo_drugs())

        for i in range(len(drugs)):  
            col1, col2, col3 = st.columns(3)
            standard = col1.selectbox(drugs[i], key=drugs[i], options=O.standard_dose())
            
            # 标准剂量 ----------------------------------------------------------
            standard_value = re.sub(' .*','',standard)
            standard_unit = re.sub('.*? ','',standard)

            if standard_unit == 'mg/㎡' and bsa != '/':
                standard_dose = int(standard_value) * float(bsa.replace(' ㎡',''))
                standard_dose = str(int(standard_dose)) + ' mg'
            elif standard_unit == 'mg/kg' and bsa != '/':
                standard_dose = int(standard_value) * int(weight)
                standard_dose = str(int(standard_dose)) + ' mg'
            elif standard_unit == 'AUC' and bsa != '/':
                standard_dose = ccr + 25
                standard_dose = standard_dose * int(standard_value)
                standard_dose = str(int(standard_dose)) + ' mg'
            else:
                standard_dose = '/'
            
            col2.text_input(drugs[i]+'丨标准剂量',key=drugs[i]+'丨标准剂量', value=standard_dose, disabled=True)
            col3.text_input(drugs[i]+'丨实际剂量',key=drugs[i]+'丨实际剂量')

    # --------------------------------------------------------------------------

    with st.expander('病历信息', expanded=True):
        output = f'患者身高 {height} cm，体重 {weight} kg，体表面积 {bsa}，'

        try:
            ccr = str(int(ccr))
            output += '血清肌酐 ' + str(scr) + ' ' + scr_unit + '，'
            output += '肌酐清除率 ' + str(ccr) + ' mL/min，'
        except:
            pass

        output += '本周期具体治疗药物及总剂量为：'

        for i, item in enumerate(drugs):
            standard = st.session_state[drugs[i]]
            standard_dose = st.session_state[drugs[i]+'丨标准剂量']
            final_dose = st.session_state[drugs[i]+'丨实际剂量']

            output += drugs[i] + ' (' + standard
            output += '; 标准剂量 ' + standard_dose 
            output += '; 实际剂量 ' + final_dose + ' mg）、'

        output = output[0:-1] + '。'
        st.caption(output.strip())
