#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request, render_template


template = '''
{对象}{事件}是怎么回事呢？
<br>{对象}相信大家都很熟悉，但是{对象}{事件}是怎么回事呢？
<br>下面就让小编带大家一起了解一下{对象}{事件}是怎么回事吧。
<br>{对象}{事件}，其实就是{对象}{事件}。大家可能会感到很惊讶，{对象}怎么会{事件}？
<br>但事实就是这样，小编也感到非常惊讶。
<br>那么这就是关于{对象}{事件}的事情啦！大家有什么想法呢？
'''

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'GET' == request.method:
        return render_template('index.html')
    else:
        form_data = request.form.to_dict()
        output = template.format(
            对象=form_data['object'],
            事件=form_data['event']
        )
        return output


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
