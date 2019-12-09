use piston_window::{PistonWindow, WindowSettings};

fn main() {
    let mut window: PistonWindow = WindowSettings::new("Hello, World!", [512; 2])
        .build()
        .unwrap();

    while let Some(e) = window.next() {
        window.draw_2d(&e, |context, graphics, _| {
            clear([0.5, 0.5, 0.5, 1.0], graphics);
            rectangle(
                [1.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 100.0, 100.0],
                context.transform,
                graphics,
            )
        });
    }
}
