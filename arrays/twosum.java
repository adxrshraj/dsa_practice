import java.util.*;

public class twosum{
    public static void main(String[] args){
        int[] arr = new arr[8];
        int[] arr = {3,2,1,6,4,2,3,6};

        HashMap<Interger,Interger> map = new HashMap<>();


        for(int j; j < arr.length; j++){
            int sum = 9;
            int first = arr[j];
            int second = sum - first;

            if(map.containsKey(second)){
                return new int[]{map.get(second),j};

                }
            map.put(arr[j], j);


            

            }



        


    }

}
