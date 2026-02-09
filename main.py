import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from prompt_builder import PromptBuilder


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Accessories Marketing Prompt Generator")
        self.resize(1000, 700)

        self._init_widgets()
        self._build_layout()
        self._connect_signals()

    # --- UI construction -------------------------------------------------
    def _init_widgets(self) -> None:
        # Product widgets
        self.style_combo = QComboBox()
        self.style_combo.addItems(
            [
                "premium commercial photography",
                "luxury fashion advertising photography",
                "editorial fashion photography",
                "lifestyle social media content",
                "e-commerce catalog photography",
                "street style fashion photography",
            ]
        )

        self.product_type_combo = QComboBox()
        self.product_type_combo.addItems(
            [
                "accessory",
                "jewelry",
                "bracelet",
                "necklace",
                "earrings",
                "ring",
                "watch",
                "sunglasses",
                "handbag",
                "wallet",
                "belt",
                "hair accessory",
            ]
        )

        self.product_material_combo = QComboBox()
        self.product_material_combo.addItems(
            [
                "gold",
                "silver",
                "rose gold",
                "stainless steel",
                "gold plated stainless steel",
                "leather",
                "vegan leather",
                "fabric",
                "beads",
                "mixed metals",
            ]
        )

        self.product_color_combo = QComboBox()
        self.product_color_combo.setEditable(True)
        self.product_color_combo.addItems(
            [
                "black",
                "silver",
                "gold",
                "rose gold",
                "black and gold",
                "silver and rose gold",
                "brown leather",
                "white and gold",
                "colorful mix",
            ]
        )
        self.product_brand_edit = QLineEdit("YOUR BRAND NAME")
        self.product_target_combo = QComboBox()
        self.product_target_combo.setEditable(True)
        self.product_target_combo.addItems(
            [
                "young adults, luxury buyers, fashion lovers",
                "luxury buyers",
                "fashion-conscious young adults",
                "minimalist style lovers",
                "gift buyers",
                "high-end jewelry customers",
                "trend-focused social media users",
            ]
        )

        # Model widgets
        self.include_model_check = QCheckBox("Include model in image")
        self.include_model_check.setChecked(True)

        self.model_gender_combo = QComboBox()
        self.model_gender_combo.addItems(
            [
                "female",
                "male",
                "unisex",
            ]
        )

        self.model_age_spin = QSpinBox()
        self.model_age_spin.setRange(16, 80)
        self.model_age_spin.setValue(25)

        self.model_ethnicity_combo = QComboBox()
        self.model_ethnicity_combo.setEditable(True)
        self.model_ethnicity_combo.addItems(
            [
                "Middle Eastern",
                "European",
                "African",
                "East Asian",
                "South Asian",
                "Latino",
                "mixed ethnicity",
            ]
        )

        self.model_pose_combo = QComboBox()
        self.model_pose_combo.setEditable(True)
        self.model_pose_combo.addItems(
            [
                "hand close-up showing bracelet",
                "wrist close-up with watch",
                "neck close-up showing necklace",
                "side profile with earrings",
                "three-quarter body shot with handbag",
                "seated pose with accessories in focus",
            ]
        )

        self.model_expression_combo = QComboBox()
        self.model_expression_combo.setEditable(True)
        self.model_expression_combo.addItems(
            [
                "elegant confident look",
                "soft smile",
                "serious luxury expression",
                "playful fashion expression",
                "mysterious confident look",
            ]
        )

        self.model_clothing_style_combo = QComboBox()
        self.model_clothing_style_combo.setEditable(True)
        self.model_clothing_style_combo.addItems(
            [
                "luxury evening dress",
                "smart casual outfit",
                "minimalist monochrome outfit",
                "business formal outfit",
                "summer dress",
                "street style fashion",
            ]
        )

        # Scene widgets
        self.scene_background_combo = QComboBox()
        self.scene_background_combo.setEditable(True)
        self.scene_background_combo.addItems(
            [
                "clean studio background, soft gradient, luxury lifestyle environment",
                "dark luxury studio background",
                "marble surface tabletop",
                "soft beige fabric background",
                "bedroom vanity setup",
                "outdoor city background, blurred",
                "beach sunset background, blurred",
            ]
        )

        self.scene_lighting_combo = QComboBox()
        self.scene_lighting_combo.setEditable(True)
        self.scene_lighting_combo.addItems(
            [
                "softbox lighting, cinematic shadows, high contrast product lighting",
                "soft cinematic lighting with highlights on jewelry",
                "natural window light, soft shadows",
                "golden hour warm lighting",
                "high contrast studio lighting",
                "dramatic spotlight on product",
            ]
        )

        self.scene_mood_combo = QComboBox()
        self.scene_mood_combo.setEditable(True)
        self.scene_mood_combo.addItems(
            [
                "luxury, elegant, modern, minimalistic",
                "premium elegant luxury",
                "romantic and feminine",
                "bold and edgy fashion",
                "clean and minimal",
                "warm and cozy lifestyle",
            ]
        )

        self.scene_props_combo = QComboBox()
        self.scene_props_combo.setEditable(True)
        self.scene_props_combo.addItems(
            [
                "perfume bottle, flowers, marble surface, glass reflections",
                "flowers, candles, silk fabric",
                "makeup items, mirror, vanity table",
                "watch box, leather wallet, cufflinks",
                "sunglasses case, magazine, coffee cup",
                "no props, clean minimal setup",
            ]
        )

        # Camera & composition (advanced)
        self.camera_enabled_check = QCheckBox("Enable advanced camera & composition")
        self.camera_enabled_check.setChecked(True)

        self.camera_type_edit = QLineEdit("DSLR commercial photography")
        self.camera_lens_edit = QLineEdit("85mm portrait lens")
        self.camera_aperture_edit = QLineEdit("f/2.8")
        self.camera_resolution_edit = QLineEdit("4K ultra detailed")

        self.composition_angle_edit = QLineEdit("close-up product focus")
        self.composition_framing_edit = QLineEdit("centered, rule of thirds")
        self.composition_dof_edit = QLineEdit("shallow depth of field")

        # Branding
        self.branding_logo_combo = QComboBox()
        self.branding_logo_combo.setEditable(True)
        self.branding_logo_combo.addItems(
            [
                "subtle watermark logo",
                "small corner logo",
                "centered logo at bottom",
                "no visible logo",
            ]
        )

        self.branding_text_overlay_combo = QComboBox()
        self.branding_text_overlay_combo.setEditable(True)
        self.branding_text_overlay_combo.addItems(
            [
                "Luxury Collection 2026",
                "New Arrivals",
                "Limited Edition",
                "Summer Collection",
                "Ramadan Collection",
                "Holiday Gift Guide",
            ]
        )

        self.branding_font_style_combo = QComboBox()
        self.branding_font_style_combo.setEditable(True)
        self.branding_font_style_combo.addItems(
            [
                "modern minimal sans-serif",
                "elegant serif",
                "bold condensed sans-serif",
                "handwritten script",
            ]
        )

        # Output
        self.output_aspect_ratio_combo = QComboBox()
        self.output_aspect_ratio_combo.addItems(
            ["1:1", "4:5", "9:16", "16:9", "3:2"]
        )

        self.output_quality_combo = QComboBox()
        self.output_quality_combo.addItems(
            ["4K ultra detailed", "8K ultra detailed", "ultra high", "standard high"]
        )

        self.output_platform_combo = QComboBox()
        self.output_platform_combo.setEditable(True)
        self.output_platform_combo.addItems(
            [
                "Instagram Post",
                "Instagram Story",
                "Instagram Reels cover",
                "Facebook Ads",
                "Website Banner",
                "E-commerce product page",
                "Instagram, Facebook Ads, Website Banner",
            ]
        )

        # Buttons and JSON preview
        self.generate_btn = QPushButton("Generate JSON")
        self.copy_btn = QPushButton("Copy to Clipboard")
        self.reset_btn = QPushButton("Reset Form")

        self.json_preview = QPlainTextEdit()
        self.json_preview.setReadOnly(True)
        font = QFont("Consolas")
        font.setPointSize(10)
        self.json_preview.setFont(font)

        # Tabs
        self.tabs = QTabWidget()

    def _build_layout(self) -> None:
        # Product & Model tab
        product_group = QGroupBox("Product")
        product_form = QFormLayout()
        product_form.addRow(QLabel("Style:"), self.style_combo)
        product_form.addRow(QLabel("Type:"), self.product_type_combo)
        product_form.addRow(QLabel("Material:"), self.product_material_combo)
        product_form.addRow(QLabel("Color(s):"), self.product_color_combo)
        product_form.addRow(QLabel("Brand name:"), self.product_brand_edit)
        product_form.addRow(QLabel("Target audience:"), self.product_target_combo)
        product_group.setLayout(product_form)

        model_group = QGroupBox("Model (optional)")
        model_form = QFormLayout()
        model_form.addRow(self.include_model_check)
        model_form.addRow(QLabel("Gender:"), self.model_gender_combo)
        model_form.addRow(QLabel("Age:"), self.model_age_spin)
        model_form.addRow(QLabel("Ethnicity:"), self.model_ethnicity_combo)
        model_form.addRow(QLabel("Pose:"), self.model_pose_combo)
        model_form.addRow(QLabel("Expression:"), self.model_expression_combo)
        model_form.addRow(QLabel("Clothing style:"), self.model_clothing_style_combo)
        model_group.setLayout(model_form)

        tab1_widget = QWidget()
        tab1_layout = QVBoxLayout(tab1_widget)
        tab1_layout.addWidget(product_group)
        tab1_layout.addWidget(model_group)
        tab1_layout.addStretch()

        # Scene & Camera tab
        scene_group = QGroupBox("Scene")
        scene_form = QFormLayout()
        scene_form.addRow(QLabel("Background:"), self.scene_background_combo)
        scene_form.addRow(QLabel("Lighting:"), self.scene_lighting_combo)
        scene_form.addRow(QLabel("Mood:"), self.scene_mood_combo)
        scene_form.addRow(QLabel("Props (comma-separated):"), self.scene_props_combo)
        scene_group.setLayout(scene_form)

        camera_group = QGroupBox("Camera & Composition (advanced)")
        camera_form = QFormLayout()
        camera_form.addRow(self.camera_enabled_check)
        camera_form.addRow(QLabel("Camera type:"), self.camera_type_edit)
        camera_form.addRow(QLabel("Lens:"), self.camera_lens_edit)
        camera_form.addRow(QLabel("Aperture:"), self.camera_aperture_edit)
        camera_form.addRow(QLabel("Resolution:"), self.camera_resolution_edit)
        camera_form.addRow(QLabel("Angle:"), self.composition_angle_edit)
        camera_form.addRow(QLabel("Framing:"), self.composition_framing_edit)
        camera_form.addRow(QLabel("Depth of field:"), self.composition_dof_edit)
        camera_group.setLayout(camera_form)

        tab2_widget = QWidget()
        tab2_layout = QVBoxLayout(tab2_widget)
        tab2_layout.addWidget(scene_group)
        tab2_layout.addWidget(camera_group)
        tab2_layout.addStretch()

        # Branding & Output tab
        branding_group = QGroupBox("Branding")
        branding_form = QFormLayout()
        branding_form.addRow(QLabel("Logo:"), self.branding_logo_combo)
        branding_form.addRow(QLabel("Text overlay:"), self.branding_text_overlay_combo)
        branding_form.addRow(QLabel("Font style:"), self.branding_font_style_combo)
        branding_group.setLayout(branding_form)

        output_group = QGroupBox("Output")
        output_form = QFormLayout()
        output_form.addRow(QLabel("Aspect ratio:"), self.output_aspect_ratio_combo)
        output_form.addRow(QLabel("Quality:"), self.output_quality_combo)
        output_form.addRow(QLabel("Platform(s):"), self.output_platform_combo)
        output_group.setLayout(output_form)

        tab3_widget = QWidget()
        tab3_layout = QVBoxLayout(tab3_widget)
        tab3_layout.addWidget(branding_group)
        tab3_layout.addWidget(output_group)
        tab3_layout.addStretch()

        self.tabs.addTab(tab1_widget, "Product & Model")
        self.tabs.addTab(tab2_widget, "Scene & Camera")
        self.tabs.addTab(tab3_widget, "Branding & Output")

        # Buttons and preview at bottom
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.generate_btn)
        buttons_layout.addWidget(self.copy_btn)
        buttons_layout.addWidget(self.reset_btn)
        buttons_layout.addStretch()

        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.addWidget(self.tabs)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(QLabel("Generated JSON prompt:"))
        main_layout.addWidget(self.json_preview, stretch=1)

        self.setCentralWidget(main_widget)

    def _connect_signals(self) -> None:
        self.include_model_check.stateChanged.connect(self._update_model_enabled)
        self.camera_enabled_check.stateChanged.connect(self._update_camera_enabled)
        self.generate_btn.clicked.connect(self.on_generate_clicked)
        self.copy_btn.clicked.connect(self.on_copy_clicked)
        self.reset_btn.clicked.connect(self.on_reset_clicked)

        # Initialize enabled states
        self._update_model_enabled()
        self._update_camera_enabled()

    # --- State helpers ---------------------------------------------------
    def _update_model_enabled(self) -> None:
        enabled = self.include_model_check.isChecked()
        for widget in [
            self.model_gender_combo,
            self.model_age_spin,
            self.model_ethnicity_combo,
            self.model_pose_combo,
            self.model_expression_combo,
            self.model_clothing_style_combo,
        ]:
            widget.setEnabled(enabled)

    def _update_camera_enabled(self) -> None:
        enabled = self.camera_enabled_check.isChecked()
        for widget in [
            self.camera_type_edit,
            self.camera_lens_edit,
            self.camera_aperture_edit,
            self.camera_resolution_edit,
            self.composition_angle_edit,
            self.composition_framing_edit,
            self.composition_dof_edit,
        ]:
            widget.setEnabled(enabled)

    # --- Data collection & validation ------------------------------------
    def _collect_form_data(self) -> dict:
        form = {
            "style": self.style_combo.currentText(),
            # Product
            "product_type": self.product_type_combo.currentText(),
            "product_material": self.product_material_combo.currentText(),
            "product_color": self.product_color_combo.currentText().strip(),
            "product_brand_name": self.product_brand_edit.text().strip(),
            "product_target_audience": self.product_target_combo.currentText().strip(),
            # Model
            "include_model": self.include_model_check.isChecked(),
            "model_gender": self.model_gender_combo.currentText(),
            "model_age": str(self.model_age_spin.value()),
            "model_ethnicity": self.model_ethnicity_combo.currentText().strip(),
            "model_pose": self.model_pose_combo.currentText().strip(),
            "model_expression": self.model_expression_combo.currentText().strip(),
            "model_clothing_style": self.model_clothing_style_combo.currentText().strip(),
            # Scene
            "scene_background": self.scene_background_combo.currentText().strip(),
            "scene_lighting": self.scene_lighting_combo.currentText().strip(),
            "scene_mood": self.scene_mood_combo.currentText().strip(),
            "scene_props": self.scene_props_combo.currentText().strip(),
            # Camera & composition
            "camera_enabled": self.camera_enabled_check.isChecked(),
            "camera_type": self.camera_type_edit.text().strip(),
            "camera_lens": self.camera_lens_edit.text().strip(),
            "camera_aperture": self.camera_aperture_edit.text().strip(),
            "camera_resolution": self.camera_resolution_edit.text().strip(),
            "composition_angle": self.composition_angle_edit.text().strip(),
            "composition_framing": self.composition_framing_edit.text().strip(),
            "composition_depth_of_field": self.composition_dof_edit.text().strip(),
            # Branding
            "branding_logo": self.branding_logo_combo.currentText().strip(),
            "branding_text_overlay": self.branding_text_overlay_combo.currentText().strip(),
            "branding_font_style": self.branding_font_style_combo.currentText().strip(),
            # Output
            "output_aspect_ratio": self.output_aspect_ratio_combo.currentText(),
            "output_quality": self.output_quality_combo.currentText(),
            "output_platform": self.output_platform_combo.currentText().strip(),
        }
        return form

    def _validate_form(self, form: dict) -> bool:
        missing = []
        if not form["product_brand_name"]:
            missing.append("Brand name")
        if not form["product_type"]:
            missing.append("Product type")
        if not form["output_aspect_ratio"]:
            missing.append("Output aspect ratio")
        if not form["output_quality"]:
            missing.append("Output quality")
        if not form["output_platform"]:
            missing.append("Output platform")

        if missing:
            QMessageBox.warning(
                self,
                "Missing information",
                "Please fill in the following fields:\n- "
                + "\n- ".join(missing),
            )
            return False
        return True

    # --- Slots -----------------------------------------------------------
    def on_generate_clicked(self) -> None:
        form = self._collect_form_data()
        if not self._validate_form(form):
            return
        json_str = PromptBuilder.build_prompt(form)
        self.json_preview.setPlainText(json_str)

    def on_copy_clicked(self) -> None:
        text = self.json_preview.toPlainText()
        if not text.strip():
            QMessageBox.information(
                self,
                "Nothing to copy",
                "Please generate a JSON prompt first.",
            )
            return
        QApplication.clipboard().setText(text)
        QMessageBox.information(self, "Copied", "JSON prompt copied to clipboard.")

    def on_reset_clicked(self) -> None:
        self.__init__()  # Rebuild the UI to restore defaults


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

