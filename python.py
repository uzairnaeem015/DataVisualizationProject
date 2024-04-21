def main(st, data, iframe_style):
    # Add content for home page
    st.subheader('Total number of charges w.r.t Program - using python')

    # Calculate the number of pickups by hour
    hourly_pickups = data.groupby(data['program']).size()

    st.bar_chart(hourly_pickups)