---
id: 96
title: "על הבעיה המסובכת של מציאת מחט בערימת שחת"
date: 2007-12-16 00:15:53
layout: post
categories: 
  - תורת הסיבוכיות
---
הבעיה של ריקון האוקיינוס בעזרת מסננת היא בלתי כריעה - לא ב-<a href="http://en.wikipedia.org/wiki/R_%28complexity%29">R</a>. הבעיה של שחיקת כדור ברזל בגודלו של כדור הארץ בידי זבוב שנוחת עליו אחת למיליון שנים היא כריעה (כלומר, הכדור יישחק בסופו של דבר ויהפוך לאבק), אבל כנראה שלא ניתן לפתרון ב<a href="http://he.wikipedia.org/wiki/%D7%96%D7%9E%D7%9F_%D7%A8%D7%99%D7%A6%D7%94_%D7%A4%D7%95%D7%9C%D7%99%D7%A0%D7%95%D7%9E%D7%99">זמן פולינומי</a> (פולינומי במה? נו, ברדיוס הכדור או משהו, למה להיטפל). לעומתן באה ועולה בעיית מציאת מחט בערימת שחת.

מכיוון שאנחנו מדברים על בעיות הכרעה (בעיות שצריך לתת להן תשובת "כן" או "לא"), בואו נניח מעכשיו שעושים לי את החיים יותר קלים ואומרים שאני רק צריך להגיד האם בערימת שחת נתונה יש מחט או אין מחט.

שלא יהיה ספק; זו בעיה קשה, קשה מאוד. אין לי שמץ של מושג איך לפתור אותה בצורה יעילה. יש לי רק פתרון אחד: שלח יד אל תוך הערימה ותפוס משהו. תפסת את המחט? אחלה. אם לא, זרוק הרחק בצד את מה שכן תפסת, ותנסה שוב.  בסופו של דבר או שתתגלה המחט, או שכל הערימה תועבר, ואז יהיה ברור לי שאין בה מחט.

אז מה נשתנה? מה כן מייחד את הבעיה הזו? ש<strong>אם</strong> אכן יש מחט בערימה, ו<strong>אם</strong> מישהו יבוא וייתן לי "רמז", אני אוכל, באמצעות הרמז הזה, לוודא שאכן יש מחט בערימה. מהו הרמז? למשל, המיקום המדוייק של המחט בערימה.

במבט ראשון, זה נראה כמו רמאות סטנדרטית. מה הטעם ב"רמז" שכזה? מי שיודע את הרמז יודע את התשובה, אז שיילך ויפתור בעצמו את הבעיה, וחסל. ובכלל, מאיפה <strong>הוא</strong> גילה איפה נמצאת המחט?

בפועל, סיטואציות שכאלה אינן כה מופרכות גם במציאות. דוגמה פרקטית קלאסית היא מערכת ההצפנה <a href="http://he.wikipedia.org/wiki/RSA">RSA</a>. אמנם, כאן זו לא בעיית כן/לא, אבל הרעיון דומה: כוחה של RSA טמון בכך שמי שיצר את המערכת הגריל שני ראשוניים, p,q, כפל אותם, ופרסם בפומבי את המכפלה, n=pq. כעת, הצפנה היא קלה לכולם בהינתן n (ועוד פרמטר נוסף e שאינו רלוונטי לענייננו), אבל פיענוח בהינתן שרק n ידוע לך היא בעיה קשה. קשה כמו מציאת מחט בערימת שחת. לעומת זאת, אם יש לך "רמז" דוגמת הפירוק של n לשני גורמיו (ומציאת פירוק שכזה היא בעצמה בעיה קשה), הרי שאתה יכול לפענח הצפנות בקלות. אם כן, כאן הסיטואציה היא שאתה עצמך יצרת עבורך את הרמז.

דרך אחרת לחשוב על כל העסק הוא בתור <strong>מערכת הוכחה</strong>: יש טענת "כן/לא" שמתייחסת לקבוצת אובייקטים מסויימים - למשל, הטענה "המספר n הוא פריק" שמתייחסת לקבוצת המספרים השלמים. כעת נתון לנו n ספציפי, ואיזה ברנש - נניח שקוראים לו בוב - מנסה לשכנע אותנו שהמספר הזה פריק. כדי שמערכת ההוכחה צריכה להיות מהסוג שעליו דיברתי קודם, היא צריכה לקיים שתי תכונות:

1) אם n אכן פריק, בוב צריך להיות מסוגל לשכנע אותנו בכך, תמיד, תוך התחשבות בכך שכוח החישוב שלנו מוגבל.

2) אם n אינו פריק, אסור שבוב יצליח לשכנע אותנו שההפך נכון - כלומר, אסור שבוב יצליח "לעבוד" עלינו, ולא משנה כמה הוא ינסה.

במקרה הזה אכן קיימת כזו מערכת הוכחה - כלומר, הגדרה אלגוריתמית לפרוטוקול שצריך להתקיים בינינו ובין בוב כדי שהתכונות הנ"ל יתקיימו: הפרוטוקול הוא פשוט "בוב שולח לנו x שגדול מ-1 וקטן מ-n. אנו בודקים אם x מחלק את n. אם כן, אנחנו משתכנעים ש-n פריק. אחרת, אנחנו אומרים לבוב ללכת לכל הרוחות". בבירור אם n פריק בוב יוכל לשכנע אותנו על ידי שליחת מחלק של n; אם לעומת זאת n לא פריק, לא משנה מה בוב יעשה - לא נשתכנע.

לקבוצה של כל הבעיות שקיימת בשבילם מערכת הוכחה מהסוג הזה קוראים <a href="http://he.wikipedia.org/wiki/NP">NP</a>. פשר השם הזה הוא "Nondeterministic Polynomial". ה-Polynomial בא לציין שאנחנו מוגבלים לחישובים "יעילים" (שפרק הזמן המקסימלי שהם דורשים חסום על ידי פולינום באורך הקלט). באשר ל-Nondeterministic, הוא מגיע מהגדרה שקולה (ומעניינת לא פחות) ל-NP, שעליה אדבר בפוסט הבא.

האם הקבוצה הזו מעניינת? כן, מאוד. למעשה, היא אולי הקבוצה המעניינת ביותר בתורת הסיבוכיות (אם כי קרוב לודאי שתכף יבוא מבוגר אחראי וינזוף בי על הטענה המופרכת הזו). אישוש כלשהו לכך אפשר למצוא בבעיית <a href="http://he.wikipedia.org/wiki/P%3DNP">P=NP</a> (זה שוויון בין שתי ה<strong>קבוצות</strong> P ו-NP, שהצגתי בפוסט הזה והקודם - התחכמויות כמו "כן, אם ורק אם N=1" כבר מזמן הפסיקו להצחיק), שהיא כנראה הבעיה המפורסמת ביותר במדעי המחשב (יש מבוגר אחראי בסביבה?), ואישוש <strong>כלשהו</strong> לטענה הזו אפשר למצוא בכך שהיא אחת משבע "<a href="http://he.wikipedia.org/wiki/%D7%91%D7%A2%D7%99%D7%95%D7%AA_%D7%94%D7%9E%D7%99%D7%9C%D7%A0%D7%99%D7%95%D7%9D">בעיות המילניום</a>" - נו, לפחות מישהו חושב שהפתרון שלה שווה מיליון דולר.

בניסוחים שהצגנו עד עכשיו, שאלת P=NP היא מאוד פשוטה - האם כל מה שניתן ל<strong>אימות</strong> בזמן פולינומי, ניתן גם לפתרון בזמן פולינומי? האם בהכרח חייבים את בוב כדי שיספק לנו "רמז", או שנוכל תמיד להסתדר בעצמנו? תחושת הבטן הראשונית שלי היא שהתשובה היא שלילית, ואם איני טועה (מבוגר אחראי...), מרבית העוסקים בתחום גם כן סבורים שהתשובה שלילית (כנראה שלא בשל תחושת בטן בלבד). עם זאת, עד היום אין שום תשובה לשאלה הזו, לא לחיוב ולא לשלילה, והיא כבר בת למעלה מ-30 שנים (אמנם, זה גיל צעיר למדי בעולם הבעיות הבלתי פתורות).

אבל P=NP לא הייתה שאלה מעניינת אלמלא NP הייתה מעניינת בפני עצמה - והיא מעניינת בפני עצמה מכיוון שקיימות המוני בעיות שידוע עליהן שהן שייכות ל-NP, אבל לא ידוע אם הן שייכות ל-P. אביא כמה דוגמאות בהמשך, כשאדבר על הקבוצה המעניינת ביותר של בעיות מתוך NP - הבעיות ה-"NP-שלמות" - הבעיות הקשות ביותר ששייכות ל-NP, אלו שאם נפתור בצורה יעילה ולו אחת מהן, הוכחנו כי P=NP.

אולם לפני כן, כדאי להכיר את ההגדרה השקולה של NP, ולצלול אל תוך העולם האי-דטרמיניסטי.
