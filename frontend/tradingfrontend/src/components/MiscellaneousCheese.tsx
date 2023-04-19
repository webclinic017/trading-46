import { useThemeContext } from "../hooks/useThemeContext";

export default function MiscellaneousCheese() {
  // define button style by darkMode
  const { darkMode } = useThemeContext();
  const btnVariant = darkMode ? "outline-highlight" : "primary";
  const shadow = darkMode ? "shadow" : "shadow-sm";

  return (
    <div className="d-flex flex-column align-items-center">
      <div
        className={`card bg-accent-1 my-3 ${shadow}`}
        style={{ width: "18rem" }}
      >
        <img
          src="https://unsplash.com/photos/kPqaqug998Y/download?force=true&w=640"
          className="card-img-top"
          alt="..."
        />
        <div className="card-body">
          <small className="text-muted">
            Photo by{" "}
            <a href="https://unsplash.com/@waldemarbrandt67w?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">
              Waldemar Brandt
            </a>{" "}
            on{" "}
            <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">
              Unsplash
            </a>
          </small>

          <h5 className="card-title mt-3">Miscellaneous chees</h5>
          <p className="card-text">
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </p>
          <button className={`btn btn-${btnVariant}`}>Cheese me up</button>
        </div>
      </div>
    </div>
  );
}
