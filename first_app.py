import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path    


## 网页标题
st.set_page_config(page_title='机器学习在药物筛选中的应用', page_icon=':robot_face:')
## 获取文件路径
current_path = Path(__file__).parent.absolute()

st.title('使用机器学习进行药物筛选的步骤', anchor='pass')