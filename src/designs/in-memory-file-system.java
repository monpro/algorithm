package designs;

import java.util.*;

class Dir {
    HashMap<String, Dir> dirs;
    HashMap<String, String> files;
    
    public Dir(){
        this.dirs = new HashMap<>();
        this.files = new HashMap<>();
    }
}

class FileSystem {

    Dir root;
    public FileSystem() {
        this.root = new Dir();
    }
    
    public List<String> ls(String path) {
        Dir curDir = root;
        List<String> result = new ArrayList<>();
        if(!path.equals("/")){
            String[] dir = path.split("/");
            int length = dir.length;
            for(int i = 1; i < length - 1; i++){
                curDir = curDir.dirs.get(dir[i]);
            }
            if(curDir.files.containsKey(dir[length - 1])){
                result.add(dir[length - 1]);
                return result;
            }else{
                curDir = curDir.dirs.get(dir[length - 1]);
            }
            
        }
        result.addAll(new ArrayList<>(curDir.dirs.keySet()));
        result.addAll(new ArrayList<>(curDir.files.keySet()));
        Collections.sort(result);
        return result;
    }
    
    public void mkdir(String path) {
        Dir curDir = root;
        String[] dir = path.split("/");
        for(int i = 1; i < dir.length; i++){
            if(!curDir.dirs.containsKey(dir[i])){
                curDir.dirs.put(dir[i], new Dir());
            }
            curDir = curDir.dirs.get(dir[i]);
        }
    }
    
    public void addContentToFile(String filePath, String content) {
        Dir curDir = root;
        String[] dir = filePath.split("/");
        int length = dir.length;
        for(int i = 1; i < length - 1; i++){
            curDir = curDir.dirs.get(dir[i]);
        }
        curDir.files.put(dir[length - 1], curDir.files.getOrDefault(dir[length - 1], "") + content);
    }
    
    public String readContentFromFile(String filePath) {
        Dir curDir = root;
        String[] dir = filePath.split("/"); 
        int length = dir.length;
        for(int i = 1; i < length - 1; i++){
            curDir = curDir.dirs.get(dir[i]);
        }
        return curDir.files.get(dir[length - 1]);
    }
}