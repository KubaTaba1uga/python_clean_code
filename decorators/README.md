Each good decorator should have:
	1.  Encapsulation, or separation of concerns.
		A good decorator should effectively seperate different
		responsibilities between what it does and what it 
		decorates. Client should be able to invoke it, without
		knowing how its logic is implemented.

	2. Orthogonality.
		The decorator logic should be independent, and as 
		decoupled as possible from the object it is decorating.

	3. Reusability.
		The decorator should can be applied to multiple types,
		if it appears on one instance of some function, it could
		be function instead. Decorator has to be generic enough.
		