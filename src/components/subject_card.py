import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(height=240, border=False):
        
        html = f"""
            <div style="
                background: white; 
                border-left: 8px solid #EB459E; 
                padding: 18px; 
                border-radius: 20px; 
                border-top: 1px solid #e2e8f0;
                border-right: 1px solid #e2e8f0;
                border-bottom: 1px solid #e2e8f0;
                margin-bottom: 10px;
                display: flex;
                flex-direction: column;
                gap: 8px;
            ">
            <div>
                <h3 style="margin: 0; color: #1e293b; font-size: 1.3rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{name}</h3>
                <p style="color: #64748b; margin: 5px 0; font-size: 0.9rem;">
                    Code : <span style="background: #E0E3FF; color: #5865F2; padding: 2px 6px; border-radius: 5px; font-weight: bold;">{code}</span> | Section : {section}
                </p>
            </div>
        """
        
        if stats:
            html += """
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
            """
            for icon, label, value in stats:
                html += f'<div style="background: #EB459E10; padding: 4px 10px; border-radius: 10px; font-size: 0.8rem; color: #475569;">{icon} <b>{value}</b> {label}</div>'
            
            html += "</div>"

        html += "</div>"  

        st.markdown(html, unsafe_allow_html=True)

        if footer_callback:
            footer_callback()
