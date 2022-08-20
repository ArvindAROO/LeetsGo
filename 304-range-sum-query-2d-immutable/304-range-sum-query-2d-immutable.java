class NumMatrix {
    int[][] mat;

    public NumMatrix(int[][] matrix) {
        this.mat = matrix;
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int sums = 0,i,j;
        for(i = row1; i <= row2; i++){
            for(j = col1; j <= col2; j++){
                sums += this.mat[i][j];
            }
        }
        return sums;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */