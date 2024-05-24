impl Solution {
    pub fn reverse_words(s: String) -> String {
        let s_vec: Vec<_> = s.split(' ').filter(|x| !x.is_empty() ).rev().collect();
        s_vec.join(" ")
    }
}
