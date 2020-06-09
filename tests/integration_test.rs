use python_runner;
use python_runner::five;

#[test]
fn test_five() {
    assert_eq!(5, five());
}