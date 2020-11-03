{
     string $selection[] = `ls -os -fl`;

    string $vertexNames[] = `filterExpand -selectionMask 31 -expand true $selection`;

     //print $vertexNames;
     
     string $objectToInstance = $selection[0];
     
     if( `objectType $objectToInstance` == "transform" ) {
         
         string $vertex;
         for( $vertex in $vertexNames ) {
             
             string $newInstance[] = `instance $objectToInstance`;
             
             vector $position = `pointPosition -w $vertex`;
             
             move -a -ws ($position.x) ($position.y) ($position.z) $newInstance;
         }
         
     } else {
         
         print "Please ensure the first object  you select is a transform.";
     }
}
