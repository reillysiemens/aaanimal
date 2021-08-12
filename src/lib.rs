mod adjectives;
mod animals;

use adjectives::ADJECTIVES;
use animals::ANIMALS;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, seq::SliceRandom};

/// TODO Module documentation.
#[pymodule]
fn aaanimal(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    /// TODO Function documentation. Is the text_signature correct?
    #[pyfn(m)]
    #[pyo3(
        name = "generate",
        text_signature = "(adjectives=2, animals=1, separator='-')"
    )]
    fn generate(
        animals: Option<u128>,
        adjectives: Option<u128>,
        separator: Option<&str>,
    ) -> String {
        // TODO: Could this be a global so we don't always instantiate it?
        let mut rng = ThreadRng::default();
        let mut words = String::new();
        let adjectives = adjectives.unwrap_or(2);
        let animals = animals.unwrap_or(1);
        let separator = separator.unwrap_or("-");

        for count in 0..adjectives {
            let adjective = ADJECTIVES
                .choose(&mut rng)
                .expect("Adjective array was inexplicably empty.");
            words.push_str(adjective);
            if count < adjectives - 1 {
                words.push_str(&separator);
            }
        }

        if adjectives != 0 && animals != 0 {
            words.push_str(&separator);
        }

        for count in 0..animals {
            let animal = ANIMALS
                .choose(&mut rng)
                .expect("Animal array was inexplicably empty.");
            words.push_str(animal);
            if count < animals - 1 {
                words.push_str(&separator);
            }
        }

        words
    }

    Ok(())
}
