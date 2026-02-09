const { useState } = React;

// --- Prompt building logic -----------------------------------------------

function buildPrompt(form) {
  const data = {
    task: "generate_marketing_image",
    style: form.style || "premium commercial photography",
    product: {
      type: form.productType || "accessory",
      material: form.productMaterial || "gold",
      color: form.productColor || "gold",
      brand_name: form.brandName || "YOUR BRAND NAME",
      target_audience:
        form.targetAudience || "young adults, luxury buyers, fashion lovers",
    },
    scene: {
      background:
        form.sceneBackground ||
        "clean studio background, soft gradient, luxury lifestyle environment",
      lighting:
        form.sceneLighting ||
        "softbox lighting, cinematic shadows, high contrast product lighting",
      mood:
        form.sceneMood || "luxury, elegant, modern, minimalistic",
    },
    branding: {
      logo: form.brandingLogo || "subtle watermark logo",
      text_overlay:
        form.brandingTextOverlay || "Luxury Collection 2026",
      font_style:
        form.brandingFontStyle || "modern minimal sans-serif",
    },
    output: {
      aspect_ratio: form.aspectRatio || "1:1",
      quality: form.quality || "ultra high",
      platform:
        form.platform || "Instagram, Facebook Ads, Website Banner",
    },
  };

  if (form.sceneProps) {
    const parts = form.sceneProps
      .split(",")
      .map((p) => p.trim())
      .filter(Boolean);
    if (parts.length > 0) {
      data.scene.props = parts;
    }
  }

  if (form.includeModel) {
    data.model = {
      include_model: true,
      gender: form.modelGender || "female",
      age: form.modelAge || "25",
      ethnicity: form.modelEthnicity || "",
      pose: form.modelPose || "",
      expression: form.modelExpression || "",
      clothing_style: form.modelClothingStyle || "",
    };
  }

  if (form.advancedCamera) {
    data.camera = {
      type: form.cameraType || "DSLR commercial photography",
      lens: form.cameraLens || "85mm portrait lens",
      aperture: form.cameraAperture || "f/2.8",
      resolution: form.cameraResolution || "4K ultra detailed",
    };
    data.composition = {
      angle: form.compositionAngle || "close-up product focus",
      framing: form.compositionFraming || "centered, rule of thirds",
      depth_of_field:
        form.compositionDepthOfField || "shallow depth of field",
    };
  }

  return data;
}

// --- UI components -------------------------------------------------------

function HeroSection({ onScrollToBuilder }) {
  return (
    <section className="hero">
      <div className="container hero-content">
        <div className="hero-text">
          <h1>Accessories Marketing Prompt Generator</h1>
          <p>
            Quickly build ultra-detailed JSON prompts for AI marketing
            images of jewelry, watches, handbags and more — with just a
            few clicks.
          </p>
          <button
            type="button"
            className="btn btn-primary"
            onClick={onScrollToBuilder}
          >
            Open Prompt Builder
          </button>
        </div>
        <div className="hero-preview-card">
          <h2>JSON Preview</h2>
          <pre className="hero-code">
{`{
  "task": "generate_marketing_image",
  "style": "premium commercial photography",
  "product": {
    "type": "bracelet",
    "material": "gold plated stainless steel"
  }
}`}
          </pre>
        </div>
      </div>
    </section>
  );
}

function FeaturesSection() {
  const features = [
    {
      title: "Accessory-focused",
      body: "Optimized for jewelry, watches, bracelets, necklaces, sunglasses, handbags, and more.",
    },
    {
      title: "Model & Scene options",
      body: "Fine-tune model pose, expression, and clothing, plus studio or lifestyle backgrounds.",
    },
    {
      title: "Preset-driven",
      body: "Select from high-quality presets so you type less and stay on-brand.",
    },
    {
      title: "One-click JSON copy",
      body: "Generate and copy ready-to-use JSON prompts for your AI image tools.",
    },
  ];

  return (
    <section className="section">
      <div className="container">
        <h2 className="section-title">Why use this generator?</h2>
        <div className="feature-grid">
          {features.map((f) => (
            <article key={f.title} className="feature-card">
              <h3>{f.title}</h3>
              <p>{f.body}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

function HowItWorksSection() {
  const steps = [
    "Choose your product, style, and target audience.",
    "Configure optional model, scene, and lighting presets.",
    "Fine-tune camera, composition, and branding.",
    "Generate JSON and paste it into your AI image tool.",
  ];

  return (
    <section className="section section-muted">
      <div className="container">
        <h2 className="section-title">How it works</h2>
        <ol className="how-list">
          {steps.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ol>
      </div>
    </section>
  );
}

function FieldGroup({ label, children }) {
  return (
    <div className="field-group">
      <label className="field-label">{label}</label>
      {children}
    </div>
  );
}

function PromptBuilderSection({ builderRef }) {
  const [form, setForm] = useState({
    style: "premium commercial photography",
    productType: "bracelet",
    productMaterial: "gold plated stainless steel",
    productColor: "rose gold",
    brandName: "Retaj Accessories",
    targetAudience: "fashion-conscious young adults",
    includeModel: true,
    modelGender: "female",
    modelAge: "25",
    modelEthnicity: "Middle Eastern",
    modelPose: "hand close-up showing bracelet",
    modelExpression: "elegant confident look",
    modelClothingStyle: "luxury evening dress",
    sceneBackground: "dark luxury studio background",
    sceneLighting:
      "soft cinematic lighting with highlights on jewelry",
    sceneMood: "premium elegant luxury",
    sceneProps: "perfume bottle, flowers, marble surface, glass reflections",
    advancedCamera: true,
    cameraType: "DSLR commercial photography",
    cameraLens: "85mm portrait lens",
    cameraAperture: "f/2.8",
    cameraResolution: "8K ultra detailed",
    compositionAngle: "close-up product focus",
    compositionFraming: "centered, rule of thirds",
    compositionDepthOfField: "shallow depth of field",
    brandingLogo: "subtle watermark logo",
    brandingTextOverlay: "Luxury Collection 2026",
    brandingFontStyle: "modern minimal sans-serif",
    aspectRatio: "1:1",
    quality: "8K ultra detailed",
    platform: "Instagram Ads",
  });
  const [jsonText, setJsonText] = useState("");
  const [copyMessage, setCopyMessage] = useState("");

  function handleChange(e) {
    const { name, value, type, checked } = e.target;
    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  }

  function handleGenerate() {
    if (!form.brandName.trim()) {
      alert("Please enter a brand name.");
      return;
    }
    const promptObj = buildPrompt(form);
    const text = JSON.stringify(promptObj, null, 2);
    setJsonText(text);
    setCopyMessage("");
  }

  async function handleCopy() {
    if (!jsonText.trim()) {
      alert("Generate JSON first.");
      return;
    }
    try {
      await navigator.clipboard.writeText(jsonText);
      setCopyMessage("Copied to clipboard!");
    } catch {
      setCopyMessage("Copy failed. Please copy manually.");
    }
  }

  return (
    <section className="section" ref={builderRef}>
      <div className="container">
        <h2 className="section-title">Prompt Builder</h2>
        <p className="section-subtitle">
          Choose from curated options to instantly build a detailed AI
          prompt for your accessories.
        </p>
        <div className="builder-layout">
          <form
            className="builder-form"
            onSubmit={(e) => {
              e.preventDefault();
              handleGenerate();
            }}
          >
            <fieldset className="fieldset">
              <legend>Product</legend>
              <FieldGroup label="Style">
                <select
                  name="style"
                  value={form.style}
                  onChange={handleChange}
                >
                  <option>premium commercial photography</option>
                  <option>luxury fashion advertising photography</option>
                  <option>editorial fashion photography</option>
                  <option>lifestyle social media content</option>
                  <option>e-commerce catalog photography</option>
                  <option>street style fashion photography</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Product type">
                <select
                  name="productType"
                  value={form.productType}
                  onChange={handleChange}
                >
                  <option>accessory</option>
                  <option>jewelry</option>
                  <option>bracelet</option>
                  <option>necklace</option>
                  <option>earrings</option>
                  <option>ring</option>
                  <option>watch</option>
                  <option>sunglasses</option>
                  <option>handbag</option>
                  <option>wallet</option>
                  <option>belt</option>
                  <option>hair accessory</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Material">
                <select
                  name="productMaterial"
                  value={form.productMaterial}
                  onChange={handleChange}
                >
                  <option>gold</option>
                  <option>silver</option>
                  <option>rose gold</option>
                  <option>stainless steel</option>
                  <option>gold plated stainless steel</option>
                  <option>leather</option>
                  <option>vegan leather</option>
                  <option>fabric</option>
                  <option>beads</option>
                  <option>mixed metals</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Color">
                <select
                  name="productColor"
                  value={form.productColor}
                  onChange={handleChange}
                >
                  <option>black</option>
                  <option>silver</option>
                  <option>gold</option>
                  <option>rose gold</option>
                  <option>black and gold</option>
                  <option>silver and rose gold</option>
                  <option>brown leather</option>
                  <option>white and gold</option>
                  <option>colorful mix</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Brand name">
                <input
                  type="text"
                  name="brandName"
                  value={form.brandName}
                  onChange={handleChange}
                  placeholder="Your brand name"
                />
              </FieldGroup>
              <FieldGroup label="Target audience">
                <select
                  name="targetAudience"
                  value={form.targetAudience}
                  onChange={handleChange}
                >
                  <option>
                    young adults, luxury buyers, fashion lovers
                  </option>
                  <option>luxury buyers</option>
                  <option>fashion-conscious young adults</option>
                  <option>minimalist style lovers</option>
                  <option>gift buyers</option>
                  <option>high-end jewelry customers</option>
                  <option>trend-focused social media users</option>
                </select>
              </FieldGroup>
            </fieldset>

            <fieldset className="fieldset">
              <legend>Model (optional)</legend>
              <div className="field-group-inline">
                <label className="checkbox-label">
                  <input
                    type="checkbox"
                    name="includeModel"
                    checked={form.includeModel}
                    onChange={handleChange}
                  />
                  Include model
                </label>
              </div>
              {form.includeModel && (
                <>
                  <FieldGroup label="Gender">
                    <select
                      name="modelGender"
                      value={form.modelGender}
                      onChange={handleChange}
                    >
                      <option>female</option>
                      <option>male</option>
                      <option>unisex</option>
                    </select>
                  </FieldGroup>
                  <FieldGroup label="Age">
                    <input
                      type="number"
                      min="16"
                      max="80"
                      name="modelAge"
                      value={form.modelAge}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Ethnicity">
                    <select
                      name="modelEthnicity"
                      value={form.modelEthnicity}
                      onChange={handleChange}
                    >
                      <option>Middle Eastern</option>
                      <option>European</option>
                      <option>African</option>
                      <option>East Asian</option>
                      <option>South Asian</option>
                      <option>Latino</option>
                      <option>mixed ethnicity</option>
                    </select>
                  </FieldGroup>
                  <FieldGroup label="Pose">
                    <select
                      name="modelPose"
                      value={form.modelPose}
                      onChange={handleChange}
                    >
                      <option>hand close-up showing bracelet</option>
                      <option>wrist close-up with watch</option>
                      <option>neck close-up showing necklace</option>
                      <option>side profile with earrings</option>
                      <option>
                        three-quarter body shot with handbag
                      </option>
                      <option>
                        seated pose with accessories in focus
                      </option>
                    </select>
                  </FieldGroup>
                  <FieldGroup label="Expression">
                    <select
                      name="modelExpression"
                      value={form.modelExpression}
                      onChange={handleChange}
                    >
                      <option>elegant confident look</option>
                      <option>soft smile</option>
                      <option>serious luxury expression</option>
                      <option>playful fashion expression</option>
                      <option>mysterious confident look</option>
                    </select>
                  </FieldGroup>
                  <FieldGroup label="Clothing style">
                    <select
                      name="modelClothingStyle"
                      value={form.modelClothingStyle}
                      onChange={handleChange}
                    >
                      <option>luxury evening dress</option>
                      <option>smart casual outfit</option>
                      <option>minimalist monochrome outfit</option>
                      <option>business formal outfit</option>
                      <option>summer dress</option>
                      <option>street style fashion</option>
                    </select>
                  </FieldGroup>
                </>
              )}
            </fieldset>

            <fieldset className="fieldset">
              <legend>Scene</legend>
              <FieldGroup label="Background">
                <select
                  name="sceneBackground"
                  value={form.sceneBackground}
                  onChange={handleChange}
                >
                  <option>
                    clean studio background, soft gradient, luxury lifestyle environment
                  </option>
                  <option>dark luxury studio background</option>
                  <option>marble surface tabletop</option>
                  <option>soft beige fabric background</option>
                  <option>bedroom vanity setup</option>
                  <option>outdoor city background, blurred</option>
                  <option>beach sunset background, blurred</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Lighting">
                <select
                  name="sceneLighting"
                  value={form.sceneLighting}
                  onChange={handleChange}
                >
                  <option>
                    softbox lighting, cinematic shadows, high contrast product lighting
                  </option>
                  <option>
                    soft cinematic lighting with highlights on jewelry
                  </option>
                  <option>natural window light, soft shadows</option>
                  <option>golden hour warm lighting</option>
                  <option>high contrast studio lighting</option>
                  <option>dramatic spotlight on product</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Mood">
                <select
                  name="sceneMood"
                  value={form.sceneMood}
                  onChange={handleChange}
                >
                  <option>luxury, elegant, modern, minimalistic</option>
                  <option>premium elegant luxury</option>
                  <option>romantic and feminine</option>
                  <option>bold and edgy fashion</option>
                  <option>clean and minimal</option>
                  <option>warm and cozy lifestyle</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Props">
                <select
                  name="sceneProps"
                  value={form.sceneProps}
                  onChange={handleChange}
                >
                  <option>
                    perfume bottle, flowers, marble surface, glass reflections
                  </option>
                  <option>flowers, candles, silk fabric</option>
                  <option>makeup items, mirror, vanity table</option>
                  <option>watch box, leather wallet, cufflinks</option>
                  <option>sunglasses case, magazine, coffee cup</option>
                  <option>no props, clean minimal setup</option>
                </select>
              </FieldGroup>
            </fieldset>

            <fieldset className="fieldset">
              <legend>Camera & Composition</legend>
              <div className="field-group-inline">
                <label className="checkbox-label">
                  <input
                    type="checkbox"
                    name="advancedCamera"
                    checked={form.advancedCamera}
                    onChange={handleChange}
                  />
                  Enable advanced camera & composition
                </label>
              </div>
              {form.advancedCamera && (
                <>
                  <FieldGroup label="Camera type">
                    <input
                      type="text"
                      name="cameraType"
                      value={form.cameraType}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Lens">
                    <input
                      type="text"
                      name="cameraLens"
                      value={form.cameraLens}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Aperture">
                    <input
                      type="text"
                      name="cameraAperture"
                      value={form.cameraAperture}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Resolution">
                    <input
                      type="text"
                      name="cameraResolution"
                      value={form.cameraResolution}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Angle">
                    <input
                      type="text"
                      name="compositionAngle"
                      value={form.compositionAngle}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Framing">
                    <input
                      type="text"
                      name="compositionFraming"
                      value={form.compositionFraming}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                  <FieldGroup label="Depth of field">
                    <input
                      type="text"
                      name="compositionDepthOfField"
                      value={form.compositionDepthOfField}
                      onChange={handleChange}
                    />
                  </FieldGroup>
                </>
              )}
            </fieldset>

            <fieldset className="fieldset">
              <legend>Branding & Output</legend>
              <FieldGroup label="Logo">
                <select
                  name="brandingLogo"
                  value={form.brandingLogo}
                  onChange={handleChange}
                >
                  <option>subtle watermark logo</option>
                  <option>small corner logo</option>
                  <option>centered logo at bottom</option>
                  <option>no visible logo</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Text overlay">
                <select
                  name="brandingTextOverlay"
                  value={form.brandingTextOverlay}
                  onChange={handleChange}
                >
                  <option>Luxury Collection 2026</option>
                  <option>New Arrivals</option>
                  <option>Limited Edition</option>
                  <option>Summer Collection</option>
                  <option>Ramadan Collection</option>
                  <option>Holiday Gift Guide</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Font style">
                <select
                  name="brandingFontStyle"
                  value={form.brandingFontStyle}
                  onChange={handleChange}
                >
                  <option>modern minimal sans-serif</option>
                  <option>elegant serif</option>
                  <option>bold condensed sans-serif</option>
                  <option>handwritten script</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Aspect ratio">
                <select
                  name="aspectRatio"
                  value={form.aspectRatio}
                  onChange={handleChange}
                >
                  <option>1:1</option>
                  <option>4:5</option>
                  <option>9:16</option>
                  <option>16:9</option>
                  <option>3:2</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Quality">
                <select
                  name="quality"
                  value={form.quality}
                  onChange={handleChange}
                >
                  <option>4K ultra detailed</option>
                  <option>8K ultra detailed</option>
                  <option>ultra high</option>
                  <option>standard high</option>
                </select>
              </FieldGroup>
              <FieldGroup label="Platform">
                <select
                  name="platform"
                  value={form.platform}
                  onChange={handleChange}
                >
                  <option>Instagram Post</option>
                  <option>Instagram Story</option>
                  <option>Instagram Reels cover</option>
                  <option>Facebook Ads</option>
                  <option>Website Banner</option>
                  <option>E-commerce product page</option>
                  <option>Instagram, Facebook Ads, Website Banner</option>
                  <option>Instagram Ads</option>
                </select>
              </FieldGroup>
            </fieldset>

            <div className="builder-actions">
              <button type="submit" className="btn btn-primary">
                Generate JSON
              </button>
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleCopy}
              >
                Copy JSON
              </button>
              {copyMessage && (
                <span className="copy-message">{copyMessage}</span>
              )}
            </div>
          </form>

          <div className="builder-preview">
            <h3>Generated JSON</h3>
            <pre className="code-block">
              {jsonText || "// Your JSON will appear here after you generate it."}
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-content">
        <p>© {new Date().getFullYear()} Accessories Prompt Generator</p>
        <p className="footer-note">
          Built for creating AI-ready marketing prompts for accessories.
        </p>
      </div>
    </footer>
  );
}

function App() {
  const builderRef = React.useRef(null);

  function scrollToBuilder() {
    if (builderRef.current) {
      builderRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }

  return (
    <>
      <header className="site-header">
        <div className="container header-inner">
          <div className="logo">Accessories Prompt Generator</div>
          <button
            type="button"
            className="header-cta"
            onClick={scrollToBuilder}
          >
            Try Builder
          </button>
        </div>
      </header>
      <main>
        <HeroSection onScrollToBuilder={scrollToBuilder} />
        <FeaturesSection />
        <HowItWorksSection />
        <PromptBuilderSection builderRef={builderRef} />
      </main>
      <Footer />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);

