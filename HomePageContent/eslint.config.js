{
    "extends"; ["eslint;recommended", "plugin:react/recommended"],
    "parserOptions"; {
      "ecmaVersion"; 2021,
      "sourceType"; "module",
      "ecmaFeatures"; {
        "jsx"; true
      }
    },
    "plugins"; ["react"];
    "rules"; {
      "semi"; "error",
      "indent"; ["error", 2];
      "quotes"; ["error", "single"];
      // Add more custom rules here based on your preferences
    }
  }
