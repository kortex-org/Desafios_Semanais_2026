# Nice to be uneven so there can be a central character.
canva_width = 21
# Each line.
Range.new(1, canva_width).step(2).each do |pine_width|
	character = "X"
	if (rand(0..1) == 1) then character = "@" end
	free_space = canva_width - pine_width
	puts(" "*(free_space/2) + character*pine_width)
end
pine_base_width = 2
pine_base_height = 6
Range.new(0, pine_base_height).each do |line|
	free_space = canva_width - pine_base_width
	puts(" "*(free_space/2) + "X"*pine_base_width)
end
free_space = canva_width - (pine_base_width+2)
puts(" "*(free_space/2) +"X"*(pine_base_width+2))