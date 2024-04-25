def main(st, data, iframe_style):
    st.subheader('Sample D3.JS using embedding from vizhub')
    # Use the st.write() function to display the iframe
    st.write(f'<iframe src="https://vizhub.com/uzairnaeem015/8c4aa17325e348c3bec8b27164e04931?mode=embed&embed=branded" style="{iframe_style}" scrolling="no" frameborder="no"></iframe>', unsafe_allow_html=True)
