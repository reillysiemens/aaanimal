mod adjectives;
mod animals;

use adjectives::ADJECTIVES;
use animals::ANIMALS;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, seq::SliceRandom};

/// TODO Module documentation.
#[pymodule]
fn adjective_adjective_animal(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    /// TODO Function documentation.
    #[pyfn(m, "generate")]
    #[text_signature = "(/, adjectives=2, sep='-')"]
    fn generate(adjectives: usize, sep: &str) -> String {
        let mut rng = ThreadRng::default();
        let mut words = String::new();

        for _ in 0..adjectives {
            words.push_str(ADJECTIVES.choose(&mut rng).unwrap());
            words.push_str(&sep);
        }

        words.push_str(ANIMALS.choose(&mut rng).unwrap());

        format!("{}", words)
    }

    Ok(())
}
