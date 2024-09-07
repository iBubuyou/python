import pygal
line = pygal.Line(height=400)
line.title = 'Line Chart'
line.x_labels = ('T1','T2','T3','T4','T5')
line.add('A', [1,3,5,7,9])
line.add('B', [0,2,4,6,8])
line.add('C', [1,5,9,3,7])
line.add('D', [1,7,3,9,5])
line.add('E', [2,7,1,5,8])
line.render_in_browser()