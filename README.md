# 2019_Final_Project
* 所需環境、安裝套件
    環境: python3.0
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib.animation import FuncAnimation
    from mpl_toolkits.mplot3d import Axes3D
    from scipy.integrate import solve_ivp

* 如何重現Demo時的結果 (助教會跑，若無法重現，Final將沒有分數)

    Differential Equation.ipynb
        1. 第一個區塊會import後面所需要的所有套件，以及所需要的微分算子，所以一定要執行。
        2. 接下來只要一一執行，所有的圖片就會重現，但須注意要把所有的fig.savefig()給關閉，否則會因為儲存路徑而跳錯誤(或是改成自己的路徑)。
        3. GIF是透過外部網站的GIF maker生成，執行此程式只會生成所有用來合成的圖片(我要用python生成GIF一直失敗啦QQ)。
    Advection Diffusion Equation
    	存放Advection Diffusion Equation所輸出的所有圖片以及製作完成的gif
    Diffusion Equation
        存放Diffusion Equation所輸出的所有圖片以及製作完成的gif
    Poission Equation
        存放Poission Equation所輸出的所有圖片以及製作完成的gif,此資料夾的圖片沒有在ppt上沒有作呈現
    Wave Equation
        存放Wave Equation所輸出的所有圖片以及製作完成的gif


* 分工表
    影片:N/A
    ppt:兩人共同製作
    檔案
        連育德 Differential Equation.ipynb, Advection Diffusion Equation, Diffusion Equation, Poission Equation, Wave Equation
        陳暐翰 Laplace_2D, Laplace_3D, Laplace results, Wave Equation 1D, Wave results
