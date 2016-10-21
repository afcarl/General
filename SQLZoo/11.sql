select A.CustomerID,C.AddressLine1 from CustomerAW A join CustomerAddress B 
on (A.CustomerID = B.CustomerID) 
join Address C on (B.AddressID = C.AddressID) 
where C.City = 'Dallas' and B.AddressType = 'Main Office'











select A.CustomerID,B.AddressLine1,C.ShipToAddressID from CustomerAddress A join Address B on (A.AddressID = B.AddressID) left join SalesOrderHeader C on (A.CustomerID = C.CustomerID)
where B.City = 'Dallas' and A.AddressType = 'Main Office'



112	P.O. Box 6256916	null
130	Po Box 8259024	null
165	2500 North Stemmons Freeway	null
201	Po Box 8035996	null
256