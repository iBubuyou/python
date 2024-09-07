import pygal
d = pygal.Dot(height=400, x_label_rotation=30)
d.title = 'Dot Chart'
d.x_labels = ('T1','T2','T3','T4','T5')
d.add('A', [1,3,5,7,9])
d.add('B', [0,2,4,6,8])
d.add('C', [1,5,9,3,7])
d.add('D', [1,7,3,9,5])
d.add('E', [2,7,1,5,8])
d.add('F', [-2,7,0,4,-4])
d.render_in_browser()