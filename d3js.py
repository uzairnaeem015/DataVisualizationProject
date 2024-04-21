import streamlit.components.v1 as components

def main(st, data, iframe_style):
    # st.title("PowerBI DashBoard")

    st.subheader('Sample D3.JS file')

    def load_d3js_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    d3js_code = load_d3js_file('d3.html')  # Replace with the path to your D3.js HTML file

    st.components.v1.html(d3js_code, height=600) 

    st.subheader('Some other D3.JS code')

    # Load the D3.js library
    d3_script = """
    <script src="https://d3js.org/d3.v6.min.js"></script>
    """

    # Define the D3.js visualization code
    d3_visualization = """
    <div id="chart"></div>
    <script>
    // D3.js visualization code goes here
    const data = [10, 20, 30, 40, 50];

    const svg = d3.select("#chart")
        .append("svg")
        .attr("width", 400)
        .attr("height", 400);

    svg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", (d, i) => i * 50 + 123)
        .attr("cy", 200)
        .attr("r", d => d)
        .attr("fill", "steelblue");
    </script>
    """

    # Render the D3.js visualization in Streamlit
    components.html(d3_script + d3_visualization, height=500)

    st.subheader('Sample D3.JS using embedding from vizhub')
    # Use the st.write() function to display the iframe
    st.write(f'<iframe src="https://vizhub.com/uzairnaeem015/8c4aa17325e348c3bec8b27164e04931?mode=embed&embed=branded" style="{iframe_style}" scrolling="no" frameborder="no"></iframe>', unsafe_allow_html=True)
