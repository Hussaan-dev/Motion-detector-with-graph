import pandas
from bokeh.plotting import output_file,show,figure
from bokeh.models import ColumnDataSource,HoverTool

output_file('MotionGraph.html')

dataframe=pandas.read_csv('Times.csv',parse_dates=['Start','End'])
dataframe['Start_string'] = dataframe['Start'].dt.strftime('%d-%m-%Y %H:%M:%S')
dataframe['End_string'] = dataframe['End'].dt.strftime('%d-%m-%Y %H:%M:%S')

cds=ColumnDataSource(dataframe)

f=figure(x_axis_type='datetime',height=200,width=500,sizing_mode='stretch_width')
f.yaxis[0].ticker.desired_num_ticks=1
f.yaxis.minor_tick_line_color='red'
f.xaxis.minor_tick_line_color='red'
f.title.text='Motion Graph'
f.title.text_color='blue'
f.title.text_font_style='bold'

hover=HoverTool(tooltips=[('Start','@Start_string'),('End','@End_string')])
f.add_tools(hover)

q=f.quad(left='Start',right='End',bottom=0,top=1,color='green',source=cds)
show(f)

