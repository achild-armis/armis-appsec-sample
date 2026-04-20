use v6;

my $name = %*ENV<QUERY_STRING> // '<script>alert("xss")</script>';

say "Content-type: text/html\n";
say "<html><body>";
say "<h1>Welcome $name</h1>";   # Vulnerable: reflected XSS
say "</body></html>";
