import streamlit as st 
import pandas as pd 
#import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
#color theory on data viz 

#-------- actually maybe a popover is not the best
# popover menu (the filtering menu)
#st.popover(label, *, help=None, disabled=False, use_container_width=False)
#with st.popover ('Pick a Time Period')
    #radio button instead of a checkbox
 #   red = popover.radio 
# upload to github raw user content because will be the easiest to import?? 


st.set_page_config(
    page_title="Montgomery County Spend Analysis",
    page_icon="🤑",
    layout="wide",
)
st.title('Montgomery County Spend Analysis')

# create two columns
tab1, tab2, tab3 = st.tabs(["2013-2017", "2018-2019", "2020-2023"])



df = pd.read_csv("https://raw.githubusercontent.com/sehbaw/spend_analysis_viz/main/data/top%20vendors%20-%20all.csv")
df["Fiscal Year"] = df["Fiscal Year"].round().astype(int)

# 2014 to 2017 
df_first = df[(df["Fiscal Year"] >= 2014) & (df["Fiscal Year"] <= 2017)]
print(df_first)
# 2018 to 2019
df_second = df[(df["Fiscal Year"] >= 2018) & (df["Fiscal Year"] <= 2019)]

# 2020 to 2023
df_third = df[(df["Fiscal Year"] >= 2020) & (df["Fiscal Year"] <= 2023)]

 #POP DATA TAKEN FROM https://msa.maryland.gov/msa/mdmanual/01glance/html/pop.html
population_2010 = "971,777"
population_2020 = "1,062,061" 
#change colors for each tab because going to be doing the same charts everytime???
#---------------------------------------------------------------------------tab1-----------------------------------------
        #population
#chart1 - https://plotly.com/python/horizontal-bar-charts/
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        container = st.container(border=True, height=700)
        container.header("Population of Montgomery County: 975,619 ")
        container.image("moco.jpg")
        container1 = st.container(border=True)
    
        
        fig1 = px.bar(df_first, x="Amount", y="Vendor", color="Vendor", title="Top Vendors 2013-2014")
        
        container1.plotly_chart(fig1)
    with col2:
        container2 = st.container(border=True, height=600)
        container3 = st.container(border=True, height=600)
        
        fig2 = px.bar(df_first, x="Amount", y="Expense Category", color="Expense Category", title="Top Categories 2013-2014")
        container2.plotly_chart(fig2)

        fig3 = px.line(df_first,  x="Fiscal Year",y="Amount", title="Expenses over the Years of 2014-2017")
        fig3.update_xaxes(tickvals=[2014, 2015, 2016, 2017])  # Specify the values where ticks should appear
        fig3.update_xaxes(ticktext=[" 2014", " 2015", " 2016", "2017"])  # Specify the text for the ticks
        container3.plotly_chart(fig3)


      

    
#chart2 - donut chart - https://plotly.com/python/pie-charts/
      #  labels = ['Vendor', 'Amount']
       # values = [df_first["Vendor"], df_first["Amount"]]
       # fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
       # st.plotly_chart(fig2)
       #fig = px.histogram(df, x="Amount", y="Vendor", color="Vendor", orientation='h',
        #            hover_data=df.columns, title="Top Vendors 2013-2014")


#


#-------------------------------------------TAB2-------------------------------------------------------------------------
with tab2:
    col3, col4 = st.columns(2)
    with col3:
        str = "1,062,061"
        container4 = st.container(border=True, height=700)
        container5 = st.container(border=True)

        container4.header("Population of Montgomery County: 1,062,061 ")
        container4.image("moco.jpg")
      
        
 #population image
    #chart1 - https://plotly.com/python/horizontal-bar-charts/

        fig4 = px.bar(df_second, x="Amount", y="Vendor",
                        hover_data=df.columns, title="Top Vendors 2018-2019", orientation="h")
        container5.plotly_chart(fig4)
    with col4:
         container6 = st.container(border=True, height=600)
         container7 = st.container(border=True, height=600)
         fig4 = px.bar(df_second, x="Amount", y="Expense Category", color="Expense Category",
                        hover_data=df.columns, title="Top Vendors 2018-2019", orientation="h")
         container6.plotly_chart(fig4)
    #chart3 - line chart
         fig5 = px.line(df_second, x="Fiscal Year",y="Amount", title="Expenses over the Years of 2018-2019")
         fig5.update_xaxes(tickvals=[2018, 2019, 2020])  # Specify the values where ticks should appear
         fig5.update_xaxes(ticktext=["2018", " 2019"])  # Specify the text for the ticks
         container7.plotly_chart(fig5)
 

#chart2 - donut chart - https://plotly.com/python/pie-charts/
      #  labels = ['Vendor', 'Amount']
       # values = [df_second["Vendor"], df_second["Amount"]]
        #fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    #  fig.show()
        #st.plotly_chart(fig)



# -------------- tab3
with tab3:
    col5,col6 = st.columns(2)
    with col5:
        container8 = st.container(border=True, height=700)
        container9 = st.container(border=True)

        container8.header("Population of Montgomery County: 1,062,061 ")
        container8.image("moco.jpg")


#chart1 - https://plotly.com/python/horizontal-bar-charts/
        fig5 = px.bar(df_third, x="Amount", y="Vendor", color="Vendor", title="Top Vendors 2023-2024", orientation='h')
        container9.plotly_chart(fig5)

        #chart3 - line chart
    with col6:
        container10 = st.container(border=True, height=600)
        container11 = st.container(border=True, height=600)
        fig6 = px.bar(df_third, x="Amount", y="Expense Category", 
                        hover_data=df.columns, title="Top Vendors 2020-2023", orientation="h", color_discrete_sequence=px.colors.qualitative.Antique)
        fig7 = px.line(df_third, x="Fiscal Year",y="Amount", title="Expenses over the Years 2020-2023")
        fig7.update_xaxes(tickvals=[2020, 2021, 2022, 2023, 2024])  # Specify the values where ticks should appear
        fig7.update_xaxes(ticktext=[" 2020", " 2021", " 2022", "2023","2024"])  # Specify the text for the ticks
    # fig.show()
        container10.plotly_chart(fig6)
        container11.plotly_chart(fig7)


        with st.container():
            fig7 = px.line(df_third, x="Fiscal Year",y="Amount", title="Expenses over the Years 2020-2023", color_discrete_sequence=px.colors.qualitative.Antique)
            fig7.update_xaxes(tickvals=[2020, 2021, 2022, 2023, 2024])  # Specify the values where ticks should appear
            fig7.update_xaxes(ticktext=[" 2020", " 2021", " 2022", "2023","2024"])  # Specify the text for the ticks




 