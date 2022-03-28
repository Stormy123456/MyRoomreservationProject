import matplotlib.pyplot as plt
import base64
import pandas as pd
import datetime
from io import BytesIO
from.models import employee,users,reservation,rooms,rounds,roomuser,CrudUser,banuser,roomhistorys,userinroomhistorys,testhistroys,testinroomhistroys


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Total')
    plt.hist(x)
    plt.xticks(rotation=45)
    plt.xlabel('Room')
    plt.ylabel('Number of uses')
    plt.tight_layout()
    graph = get_graph()
    return graph