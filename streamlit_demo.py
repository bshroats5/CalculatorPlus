import streamlit as st
import math
from datetime import datetime
import json

# Set page config
st.set_page_config(
    page_title="Calculator Plus Demo",
    page_icon="🧮",
    layout="centered"
)

# Initialize session state
if 'calculation_history' not in st.session_state:
    st.session_state.calculation_history = []
if 'display' not in st.session_state:
    st.session_state.display = ""

st.title("🧮 Calculator Plus - Web Demo")
st.markdown("A powerful calculator with note-taking functionality")

# Display field
display_value = st.text_input("Expression:", value=st.session_state.display, key="calc_input")

# Button layout using columns
col1, col2, col3, col4 = st.columns(4)

# Number buttons and basic operations
with col1:
    if st.button("7", key="7"):
        st.session_state.display += "7"
        st.rerun()
    if st.button("4", key="4"):
        st.session_state.display += "4"
        st.rerun()
    if st.button("1", key="1"):
        st.session_state.display += "1"
        st.rerun()
    if st.button("0", key="0"):
        st.session_state.display += "0"
        st.rerun()

with col2:
    if st.button("8", key="8"):
        st.session_state.display += "8"
        st.rerun()
    if st.button("5", key="5"):
        st.session_state.display += "5"
        st.rerun()
    if st.button("2", key="2"):
        st.session_state.display += "2"
        st.rerun()
    if st.button(".", key="dot"):
        st.session_state.display += "."
        st.rerun()

with col3:
    if st.button("9", key="9"):
        st.session_state.display += "9"
        st.rerun()
    if st.button("6", key="6"):
        st.session_state.display += "6"
        st.rerun()
    if st.button("3", key="3"):
        st.session_state.display += "3"
        st.rerun()
    if st.button("C", key="clear"):
        st.session_state.display = ""
        st.rerun()

with col4:
    if st.button("/", key="div"):
        st.session_state.display += "/"
        st.rerun()
    if st.button("*", key="mul"):
        st.session_state.display += "*"
        st.rerun()
    if st.button("-", key="sub"):
        st.session_state.display += "-"
        st.rerun()
    if st.button("+", key="add"):
        st.session_state.display += "+"
        st.rerun()

# Advanced functions
st.subheader("Advanced Functions")
col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("sin", key="sin"):
        st.session_state.display += "sin("
        st.rerun()
    if st.button("(", key="lparen"):
        st.session_state.display += "("
        st.rerun()

with col6:
    if st.button("cos", key="cos"):
        st.session_state.display += "cos("
        st.rerun()
    if st.button(")", key="rparen"):
        st.session_state.display += ")"
        st.rerun()

with col7:
    if st.button("tan", key="tan"):
        st.session_state.display += "tan("
        st.rerun()
    if st.button("√", key="sqrt"):
        st.session_state.display += "sqrt("
        st.rerun()

with col8:
    if st.button("π", key="pi"):
        st.session_state.display += str(math.pi)
        st.rerun()
    if st.button("^", key="pow"):
        st.session_state.display += "**"
        st.rerun()

# Update display from input
if display_value != st.session_state.display:
    st.session_state.display = display_value

# Calculate button
if st.button("🟰 Calculate", key="calculate", type="primary"):
    try:
        expr = st.session_state.display
        
        # Replace math functions
        expr = expr.replace('^', '**')
        expr = expr.replace('sqrt', 'math.sqrt')
        expr = expr.replace('sin', 'math.sin')
        expr = expr.replace('cos', 'math.cos')
        expr = expr.replace('tan', 'math.tan')
        expr = expr.replace('exp', 'math.exp')
        expr = expr.replace('log', 'math.log')
        expr = expr.replace('π', str(math.pi))

        # Safely evaluate
        result = eval(expr, {"__builtins__": None}, 
                      {"math": math, "abs": abs})
        
        # Format result
        result_str = f"{result:.4f}" if isinstance(result, float) else str(result)
        
        # Show result
        st.success(f"Result: {result_str}")
        st.session_state.display = result_str
        
        # Add note section
        note = st.text_input("Add a note for this calculation:", key=f"note_{len(st.session_state.calculation_history)}")
        
        if st.button("Save Calculation", key="save_calc"):
            calculation_entry = {
                "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "expression": st.session_state.display,
                "result": result_str,
                "note": note
            }
            st.session_state.calculation_history.append(calculation_entry)
            st.success("Calculation saved!")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")

# History section
if st.session_state.calculation_history:
    st.subheader("📝 Calculation History")
    
    with st.expander("View History"):
        for i, entry in enumerate(reversed(st.session_state.calculation_history)):
            st.write(f"**{entry['date']}**")
            st.write(f"Expression: `{entry['expression']}`")
            st.write(f"Result: `{entry['result']}`")
            if entry['note']:
                st.write(f"Note: {entry['note']}")
            st.divider()
    
    # Download history as JSON
    history_json = json.dumps(st.session_state.calculation_history, indent=2)
    st.download_button(
        label="📥 Download History",
        data=history_json,
        file_name=f"calculator_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json"
    )

# Footer
st.markdown("---")
st.markdown("💡 **Demo Features**: All calculator functions from the desktop app, plus web-based note saving and history download!")
