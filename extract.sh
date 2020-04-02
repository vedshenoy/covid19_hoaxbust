awk '{if($1=="दावा:") print $1}' marathi.txt   > string1_marathi.txt
awk '{if($1=="दावा:") {for(ii=2; ii<=NF; ii++) printf "%s ", $ii; print ""} }' marathi.txt   > string2_marathi.txt
awk '{if($1=="निर्णय:") print $1}' marathi.txt   > string3_marathi.txt
awk '{if($1=="निर्णय:") {for(ii=2; ii<=NF; ii++) printf "%s ", $ii; print ""}}' marathi.txt   > string4_marathi.txt
awk '{if($1=="का?:") print $1}' marathi.txt   > string5_marathi.txt
awk 'BEGIN{pp=0}{if($1=="का?:"){pp = 1; next;}else{ if($1=="अधिक" && pp==1){ pp=0; print "=========="}}; if(pp==1)print $0}' marathi.txt   > string6_marathi.txt
