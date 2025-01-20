function minkowski_distance(v1,v2,p)
#Assumes v1 and v2 of same length.
# Returns the Minkowski distance of order p between v1 and v2
if length(v1) != length(v2)
	error("The lenght of v1 and v2 should be same");
end
dist=0.0;
for  j=1:length(v1)
dist+=abs(v1[j]-v2[j])^p;
end
return dist^(1.0/p)
end