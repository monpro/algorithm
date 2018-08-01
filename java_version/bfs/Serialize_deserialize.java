package bfs;

import java.util.ArrayList;

//will seriazlize to the following{1,2,3,#,4,5,#}
//
public class Serialize_deserialize {
    public String serialize(TreeNode root) {
        if(root == null){
            return "{}";
        }
        ArrayList<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        for(int i=0; i < queue.size();i++){
            TreeNode node = queue.get(i);
            if(node == null){
                continue;
            }
            queue.add(node.left);
            queue.add(node.right);
        }

        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append(queue.get(0).val);
        for(int i = 1; i < queue.size();i++){
            if(queue.get(i) == null){
                sb.append(",#");
            }
            else{
                sb.append(",");
                sb.append(queue.get(i).val);
            }
        }
        sb.append("}");
        return sb.toString();


    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("{}")) {
            return null;
        }
        String[] vals = data.substring(1, data.length() - 1).split(",");
        ArrayList<TreeNode> queue = new ArrayList<TreeNode>();
        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));
        queue.add(root);
        int index = 0;
        boolean isLeftChild = true;
        for(int i = 1; i < vals.length;i++){
            if(!vals[i].equals("#")){
                TreeNode node = new TreeNode(Integer.parseInt(vals[i]));
                if(isLeftChild){
                    queue.get(index).left = node;
                }else{
                    queue.get(index).right = node;
                }
                queue.add(node);
            }
            if(!isLeftChild){
                index++;
            }
            isLeftChild = !isLeftChild;
        }
        return root;
    }
}
