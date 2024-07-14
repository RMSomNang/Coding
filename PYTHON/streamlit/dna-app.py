import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

st.write("""
# This is the DNA Web App
""")

logo = Image.open('dna-logo.jpg')
st.image(logo, use_column_width=True)

st.write("""
## DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
""")

# create st header
st.header("Enter DNA Sequence")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence Input", sequence_input, height=150)

sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = "".join(sequence)

st.write("""
***
""")

# Print the input DNA Sequence
st.header("INPUT (DNA Query)")
sequence

# DNA Nucleotide Count
st.header("OUTPUT (DNA Nucleotide Count)")

# 1. Print Dictionary
st.subheader("1. Print Dictionary")
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('C', seq.count('C')),
        ('G', seq.count('G')),
    ])
    return d

# Assign DNA nucleotide count of Sequence through DNA_nucleotide_count function to X
# X_label = list(X)
# X_values = list(X.values())
X = DNA_nucleotide_count(sequence)
X

# 2. Print Text

count_A = str(X["A"])
count_T = str(X["T"])
count_G = str(X["G"])
count_C = str(X["C"])

st.subheader("2. Print Text")
st.write("There are " + count_A + " adenine (A)")
st.write("There are " + count_T + " thymine (T)")
st.write("There are " + count_C + " cytosine (C)")
st.write("There are " + count_G + " guanine (G)")

# 3. Display DataFrame
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient="index")
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

# 4. Display Bar Chart
# st.subheader("Display Bar Chart")
# bar_chart = alt.Chart(df).mark_bar().encode(
#     x = 'nucleotide',
#     y = 'count'
# )
# bar_chart = bar_chart.properties(
#     width = alt.Step(80) #width of bar chart
# )

# st.write(bar_chart)

# 4. Display Bar Chart
st.subheader("Display Bar Chart")
bar_chart = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',
    y = 'count'
)
bar_chart = bar_chart.properties(
    width = alt.Step(60)
)
st.write(bar_chart)