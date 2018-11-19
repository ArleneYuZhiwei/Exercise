## Brute Force 94MS
    #include<iostream>
    #include<cstdio> 
    #define ll long long 
    #define fo(i,j,n) for(register int i=j; i<=n; ++i)
    using namespace std;
    int a[105][105],n;
    int sum[105][105];
    // Prefix sum of the matrix
    void init(){
      fo(i,1,n){
        fo(j,1,n){
          sum[i][j] = sum[i-1][j] + sum[i][j-1] + a[i][j] - sum[i-1][j-1];
        }
      }
    }
    int query(int x1, int y1, int x2, int y2){
      return sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1];
    }
    void solve(){
      int MAX = -1e8;
      fo(x1,1,n){
        fo(y1,1,n){
          fo(x2,x1,n){
            fo(y2,y1,n){
              int t = query(x1,y1,x2,y2);
              if(t>MAX) {
                MAX = t;
              }
            }
          }
        }
      }
      printf("%d\n",MAX);
    }
    int main(){
      scanf("%d",&n);
      fo(i,1,n){
        fo(j,1,n){
          scanf("%d",&a[i][j]);
        }
      }
      init();
      solve();
      return 0;
    }
## Greedy O(n^3) 16MS
    #include<iostream>
    #include<cstdio>
    #include<cstring>
    #define ll long long
    #define fo(i,j,n) for(register int i=j; i<=n; ++i)
    using namespace std;
    const int maxn = 1e4;
    int mp[maxn][maxn],n;
    int d[maxn];
    void solve(){
      int ans = mp[1][1];
      fo(i,1,n){ // i-start row 
        memset(d,0,sizeof(d)); 
        fo(j,i,n){ // j-end row
          fo(k,1,n){ // k-columns
            d[k] += mp[j][k]; // d[k] column k  summation of the row i~j
          }

          // 1-D max continuous sequence 
          int sum = 0;
          fo(k,1,n){
            sum += d[k];
            ans = max(ans,sum);
            if(sum<0) sum=0;
          } 
        }
      }
      printf("%d\n", ans);
    } 
    int main(){
      while(scanf("%d",&n)==1){ 
        fo(i,1,n){
          fo(j,1,n)
            scanf("%d",&mp[i][j]);
        }
        solve();
      }
      return 0;
    }
 
## Tips
1. Find the max-sequence in 1-D array:

if dp[i-1] > 0，  dp[i] = dp[i-1] + a[i]

if dp[i-1] < 0，  dp[i] = a[i]

2.For 2-D matrix:

Add the same columns in differenr rows

3.How to achieve O(n^2logn)?

Segment tree

    for r1 in range(0,N-1):
        for r2 in range(r1+1, N):
            for index, value in non_empty_items[r2]:
                segment_tree.insert(index, value)
            ans = max(ans, segment_tree.max_segment(0,N))
