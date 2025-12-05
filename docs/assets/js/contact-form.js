// Contact Form Functions
function openContactForm(productName = "", productType = "", price = "") {
  const overlay = document.getElementById("contactFormOverlay");
  const form = document.getElementById("contactForm");
  const subjectField = document.getElementById("subject");
  const productInfoField = document.getElementById("productInfo");
  const messageField = document.getElementById("message");

  // Pre-fill form based on product
  if (productName) {
    let subject = `Interesse an: ${productName}`;
    if (productType) {
      subject += ` (${productType})`;
    }
    subjectField.value = subject;
    subjectField.readOnly = true; // Make readonly for product inquiries

    let productInfo = `Produkt: ${productName}`;
    if (productType) {
      productInfo += `\nTyp: ${productType}`;
    }
    if (price) {
      productInfo += `\nPreis: ${price}`;
    }
    productInfoField.value = productInfo;

    // Pre-fill message with a template
    messageField.value = `Hallo,\n\nich interessiere mich für "${productName}" und hätte gerne mehr Informationen.\n\n`;
  } else {
    subjectField.value = "Allgemeine Anfrage";
    subjectField.readOnly = false; // Make editable for general inquiries
    productInfoField.value = "";
    messageField.value = "";
  }

  // Show overlay
  overlay.classList.add("active");
  document.body.style.overflow = "hidden";

  // Reset form states
  document.getElementById("formSuccess").style.display = "none";
  document.getElementById("formError").style.display = "none";
  form.style.display = "block";
}

function closeContactForm() {
  const overlay = document.getElementById("contactFormOverlay");
  overlay.classList.remove("active");
  document.body.style.overflow = "";

  // Reset form
  const form = document.getElementById("contactForm");
  form.reset();
}

// Close form when clicking outside
document.addEventListener("DOMContentLoaded", function () {
  const overlay = document.getElementById("contactFormOverlay");
  if (overlay) {
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) {
        closeContactForm();
      }
    });
  }

  // Handle form submission
  const form = document.getElementById("contactForm");
  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      const submitBtn = form.querySelector('button[type="submit"]');
      const btnText = submitBtn.querySelector(".btn-text");
      const btnLoading = submitBtn.querySelector(".btn-loading");

      // Show loading state
      submitBtn.disabled = true;
      btnText.style.display = "none";
      btnLoading.style.display = "inline";

      try {
        const formData = new FormData(form);
        const response = await fetch(form.action, {
          method: "POST",
          body: formData,
          headers: {
            Accept: "application/json",
          },
        });

        if (response.ok) {
          // Success
          form.style.display = "none";
          document.getElementById("formSuccess").style.display = "block";

          // Close form after 3 seconds
          setTimeout(() => {
            closeContactForm();
          }, 3000);
        } else {
          // Error
          throw new Error("Form submission failed");
        }
      } catch (error) {
        console.error("Error:", error);
        form.style.display = "none";
        document.getElementById("formError").style.display = "block";

        // Reset button state
        submitBtn.disabled = false;
        btnText.style.display = "inline";
        btnLoading.style.display = "none";

        // Show form again after 3 seconds
        setTimeout(() => {
          form.style.display = "block";
          document.getElementById("formError").style.display = "none";
        }, 3000);
      }
    });
  }
});

// Close with Escape key
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    closeContactForm();
  }
});
