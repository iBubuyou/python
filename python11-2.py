import pygal
bar = pygal.Bar (height=400)
bar.title = 'Browser Market Share (%)'
bar.add('Chorme', 71.19)
bar.add('Edge +IE', 14.85)
bar.add('Firefox', 7.60)
bar.add('Safari', 3.69)
bar.add('Other', 2.67)
bar.render_in_browser()