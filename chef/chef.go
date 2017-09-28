package main
import "fmt"

/// Points struct..we have created an array of this struct named arr..which is dynamic
type Point struct {
    x int
    y int
}

var cnt int

func chkwithorigin(a Point,b Point) float32{
    var val int
    val =(0 - b.x) * (a.y - b.y) - (a.x - b.x) * (0 - b.y)
    return float32(val)    
}

func checkinTrn(a Point,b Point,c Point) bool{
        var b1 bool
        var b2 bool
        var b3 bool
    
        var val1 float32
        var val2 float32
        var val3 float32
    
        val1=chkwithorigin(a,b)
        val2=chkwithorigin(b,c)
        val3=chkwithorigin(c,a)
        
        /// if any val is zero that means origin is not in the set
        if val1==0.0 || val2==0.0 || val3==0.0{  
               return false;
        }
        
        if val1<0.0 {
            b1=true
        }
        if val2<0.0{
            b2=true
        }
        if val3<0.0{
            b3=true
        }
    
        return ((b1 == b2) && (b2 == b3))
    
}

/// getting all subsets of 3 points of that array
func subst(arr []Point,n int, r int, index int,
							 res [3]Point,i int){
        
    if index == r {
                    var flag bool
                    flag=checkinTrn(res[0],res[1],res[2])
                    ///if flag true that means origin is in within that point sets
                    if flag==true {
                        //fmt.Println(res);
                        cnt++;
                    }
        
                    return
		}
    
       if i >= n {
		  return;
       }
		/// adding 3 points data to each res
		res[index] = arr[i];
		subst(arr, n, r, index+1, res, i+1);

		subst(arr, n, r, index, res, i+1);
    
}


func countchk(arr[] Point,n int) {
	var res [3]Point
	subst(arr,n, 3, 0, res, 0)
}


func main() {
    var n int
    fmt.Scan(&n)
    
    /// create point array
    arr := make([]Point,0)
    
    for i := 0; i < n; i++ {
		var p1 int
        var p2 int
        
        /// scanning number from console
        fmt.Scan(&p1)
        fmt.Scan(&p2)
        
        /// appending point array
        arr = append(arr, Point{p1, p2})
        
        if num := i; num < 2 {
            fmt.Println(0)
        } else {
            countchk(arr,i+1)
            ///print the count as output if origins are in points set
            fmt.Println(cnt)
            /// resetting the count for next iteration
            cnt=0
        }
        
        
	}
}


//// test cases list
/*
TC:1
6
2 3
3 0
-1 -1
3 4
4 1
5 5



TC:2
6
2 3
3 0
-2 -1
3 4
4 1
5 5


TC:3

10
1 3
2 10
1 -5
1 6
2 3
3 0
-2 -1
3 4
4 1
5 5


*/