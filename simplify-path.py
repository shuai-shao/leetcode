class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        dirs = path.split('/')
        rst = []
        for dir in dirs:
            if dir in ['/','','.']:
                continue
            if dir == '..':
                rst = rst[:-1]
            else:
                rst.append(dir)
        return '/' + '/'.join(rst)
