# SQL Query Generator using Google Gemini API
# Developer: Saumya Singh

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY="YOUR_API_KEY"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')
def main():
    st.set_page_config(page_title="SQL QUERY GENERATOR",page_icon="robot")
    st.markdown(
        """
        
            <div style="text-align: center;">
                <h1>SQL Query Generator</h1>
                <h3>I can generate SQL queries for you!</h3>
                <p>This tool is a simple tool that allows you to generate SQL queries based on your data.</p>
        
        

            </div>
        """,
        unsafe_allow_html=True,


      )
    text_input=st.text_area("Enter your query in plain text")
    submit=st.button("Generate Sql query:")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                Create a SQL query snippet using the below text:
                ```
                    {text_input}
                ```
                I just want a SQL Query.





            """
            formatted_template=template.format(text_input=text_input)
            
            response=model.generate_content(formatted_template)
            sql_query=response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            

            expected_output="""
                what would be expected response:
                ```
                    {sql_query}
                ```
                provide sample tabular response with no explanation.

            """
            expected_output_formatted=expected_output.format(sql_query=sql_query)
            eoutput=model.generate_content(expected_output_formatted)
            eoutput=eoutput.text
            

            explanation="""
                explain this sql query:
                ````
                    {sql_query}
                ````
                please provide with simplest explanation.

            """
            explanation_formatted=explanation.format(sql_query=sql_query)
            explanation=model.generate_content(explanation_formatted)
            explanation=explanation.text

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code(sql_query, language="sql")
                st.success("Expected Output of this SQL Query will be:")
                st.markdown (eoutput)
                st.success("Explanation of this SQL Query:")
                st.markdown(explanation)

            


            

        
main()    

