#!/usr/bin/perl 

use lib qw(./lib);

use Google::reCAPTCHA::v3; 

use Data::Dumper; 

my $rec = Google::reCAPTCHA::v3->new({
	-secret => '',
}); 
my $r = 

	$rec->request(
		{ 
			-response => "", 
		}
	);
	
	print "\n";
	print Dumper($r); 
	print "\n";
	#print $r->{success};
#	print "\n";
	 
print "ok.\n";