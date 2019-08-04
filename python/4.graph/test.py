
def ParseGraphVertexEdge(file):
    with open(file, 'r') as fw:
        read_data = fw.read()
        res = read_data.splitlines(False)

        def ParseV(v_str):
            '''
            @type v_str: string
            :param v_str:
            :return:
            '''
            return [int(i) for i in v_str.split()]

        v = int(res[0])
        edges = [ParseV(vstr) for vstr in res[1:]]

        return v, edges

if __name__ == '__main__':
    v, edges = ParseGraphVertexEdge('graph.in')
    print(v, edges)