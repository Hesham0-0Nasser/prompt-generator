import json
from typing import Any, Dict, List


class PromptBuilder:
    """Builds the JSON prompt for accessories marketing images."""

    @staticmethod
    def _split_to_list(value: str) -> List[str]:
        if not value:
            return []
        parts = [p.strip() for p in value.split(",")]
        return [p for p in parts if p]

    @classmethod
    def build_prompt(cls, form: Dict[str, Any]) -> str:
        """
        Build the JSON string based on flattened form data.

        Expected keys in `form`:
          - style
          - product_type, product_material, product_color,
            product_brand_name, product_target_audience
          - include_model (bool) and optional model_* fields
          - scene_background, scene_lighting, scene_mood, scene_props
          - camera_enabled (bool) and camera_* fields
          - composition_* fields
          - branding_logo, branding_text_overlay, branding_font_style
          - output_aspect_ratio, output_quality, output_platform
        """
        data: Dict[str, Any] = {
            "task": "generate_marketing_image",
            "style": form.get("style") or "premium commercial photography",
        }

        # Product
        product: Dict[str, Any] = {
            "type": form.get("product_type") or "accessory",
            "material": form.get("product_material") or "gold",
            "color": form.get("product_color") or "gold",
            "brand_name": form.get("product_brand_name") or "YOUR BRAND NAME",
            "target_audience": form.get("product_target_audience")
            or "young adults, luxury buyers, fashion lovers",
        }
        data["product"] = product

        # Model (optional)
        if form.get("include_model"):
            model: Dict[str, Any] = {
                "include_model": True,
                "gender": form.get("model_gender") or "female",
                "age": form.get("model_age") or "25",
                "ethnicity": form.get("model_ethnicity") or "",
                "pose": form.get("model_pose") or "",
                "expression": form.get("model_expression") or "",
                "clothing_style": form.get("model_clothing_style") or "",
            }
            data["model"] = model

        # Scene
        scene_props_list = cls._split_to_list(form.get("scene_props", ""))
        scene: Dict[str, Any] = {
            "background": form.get("scene_background")
            or "clean studio background, soft gradient, luxury lifestyle environment",
            "lighting": form.get("scene_lighting")
            or "softbox lighting, cinematic shadows, high contrast product lighting",
            "mood": form.get("scene_mood")
            or "luxury, elegant, modern, minimalistic",
        }
        if scene_props_list:
            scene["props"] = scene_props_list
        data["scene"] = scene

        # Camera & composition (optional / advanced)
        if form.get("camera_enabled"):
            camera: Dict[str, Any] = {}
            camera_type = form.get("camera_type") or "DSLR commercial photography"
            lens = form.get("camera_lens") or "85mm portrait lens"
            aperture = form.get("camera_aperture") or "f/2.8"
            resolution = form.get("camera_resolution") or "4K ultra detailed"
            camera.update(
                {
                    "type": camera_type,
                    "lens": lens,
                    "aperture": aperture,
                    "resolution": resolution,
                }
            )
            data["camera"] = camera

            composition: Dict[str, Any] = {
                "angle": form.get("composition_angle")
                or "close-up product focus",
                "framing": form.get("composition_framing")
                or "centered, rule of thirds",
                "depth_of_field": form.get("composition_depth_of_field")
                or "shallow depth of field",
            }
            data["composition"] = composition

        # Branding
        branding: Dict[str, Any] = {
            "logo": form.get("branding_logo") or "subtle watermark logo",
            "text_overlay": form.get("branding_text_overlay") or "Luxury Collection 2026",
            "font_style": form.get("branding_font_style") or "modern minimal sans-serif",
        }
        data["branding"] = branding

        # Output
        output: Dict[str, Any] = {
            "aspect_ratio": form.get("output_aspect_ratio") or "1:1",
            "quality": form.get("output_quality") or "ultra high",
            "platform": form.get("output_platform")
            or "Instagram, Facebook Ads, Website Banner",
        }
        data["output"] = output

        return json.dumps(data, indent=2, ensure_ascii=False)

