package problem0002

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	result := &ListNode{}
	temp := result
	v, n := 0, 0

	for {
		// Addition on the current bit
		v, n = add(l1, l2, n)
		temp.Val = v

		// Go to the next bit
		l1 = next(l1)
		l2 = next(l2)

		// If the next two digits of both numbers are nil, then end the bitwise addition operation
		if l1 == nil && l2 == nil {
			break
		}

		// Prepare the node for next operation
		temp.Next = &ListNode{}
		temp = temp.Next
	}

	// n == 1 indicates the last addition operation was carried out and a node needs to be added

	if n == 1 {
		temp.Next = &ListNode{Val: n}
	}

	return result
}

// next enters the next bit of l
func next(l *ListNode) *ListNode {
	if l != nil {
		return l.Next
	}
	return nil
}

func add(n1, n2 *ListNode, i int) (v, n int) {
	if n1 != nil {
		v += n1.Val
	}

	if n2 != nil {
		v += n2.Val
	}

	v += i

	if v > 9 {
		v -= 10
		n = 1
	}
	return
}
