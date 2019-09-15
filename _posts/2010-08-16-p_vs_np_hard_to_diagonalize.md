---
id: 716
title: "אז מדוע קשה להוכיח ש-P שונה מ-NP? (בלכסון)"
date: 2010-08-16 22:18:02
layout: post
categories: 
  - חישוביות
  - תורת הסיבוכיות
tags: 
  - בעיית P=NP
  - בעיית העצירה
  - לכסון
  - משפטי היררכייה בסיבוכיות
---
אם תבקשו ממני לתארך את הולדת מדעי המחשב התיאורטיים, אגיד שזה היה ב<a href="http://www.google.com/url?sa=t&amp;source=web&amp;cd=1&amp;ved=0CBcQFjAA&amp;url=http%3A%2F%2Fwww.thocp.net%2Fbiographies%2Fpapers%2Fturing_oncomputablenumbers_1936.pdf&amp;ei=NYppTJ2mDc-fONmQwbgF&amp;usg=AFQjCNHLCPE7ZMMOfz6ZUP2gDQYZGCoxIA&amp;sig2=VkKRrxKmGZBD-j04nHYVFw">מאמר של טיורינג</a> מ-1936 שבו הוא הציג את המודל החישובי שלו והוכיח שבעיית העצירה אינה ניתנת לפתרון על ידו. אמנם, מודלים חישוביים הוצעו קודם ותוצאות אי אפשרות הוכחו קודם, אך המאמר של טיורינג (לדעתי הלא מלומדת) הוא הראשון שתפס בצורה פשוטה ואינטואיטיבית אך מתמטית את הרעיון של חישוב; ויש משהו אירוני אך הולם בכך שלידתם של מדעי המחשב הייתה בדיוק בעיסוק בגבולותיהם - בדברים שלא ניתנים כלל לחישוב. זה כמובן אינו מקרי - הצורך להגדיר באופן מדוייק את מושג החישוב נבע בדיוק מהרצון להראות שמשהו בלתי ניתן לחישוב - שכן כדי להראות זאת צריך לומר תוצאה <strong>כללית</strong> על כל החישובים האפשריים, ולשם כך חייבים להגדיר במדוייק מה נקרא בכלל "חישוב".

ההוכחה של טיורינג (שאת הגרסה המקובלת שלה כיום <a href="http://www.gadial.net/?p=65">הצגתי כבר בעבר</a>. אמנם עסקה במודל קונקרטי, אך למעשה היא כמעט ולא השתמשה בפרטים קונקרטיים הקשורים למודל זה. התכונה המרכזית שבה נעשה שימוש הייתה העובדה שמכונת טיורינג ניתנת לתיאור באמצעות מחרוזת (רצף תווים) סופית, ושבהינתן מחרוזת תווים שכזו, מכונת טיורינג אחרת מסוגלת <strong>לבצע סימולציה</strong> של המכונה המקודדת. כל מי שמקיים תכונות אלו (ומאפשר לנו בנוסף לכך לבצע חישובים מאוד בסיסיים) חשוף להוכחה של טיורינג.

אזכיר אותה בקצרה (כפי שכל מי שיביט במאמר של טיורינג יראה, זה "לא בדיוק" מה שטיורינג אמר, אבל ביד חופשית שכזו נהוג להשתמש כל הזמן כל עוד לא מתיימרים לעסוק בהיסטוריה של המתמטיקה): נניח שיש לנו מכונה {% equation %}Q{% endequation %} שבהינתן מכונה אחרת {% equation %}M{% endequation %} וקלט עבורה {% equation %}x{% endequation %} אומרת האם {% equation %}M{% endequation %} עוצרת בריצתה על {% equation %}x{% endequation %} או שלא. כעת נבנה מכונה {% equation %}U{% endequation %} שעל קלט {% equation %}x{% endequation %} מזינה ל-{% equation %}Q{% endequation %} את הזוג {% equation %}\left(x,x\right){% endequation %} (כלומר, שואלת את {% equation %}Q{% endequation %} "מה עושה המכונה המקודדת בתור {% equation %}x{% endequation %} כשמריצים אותה על עצמה?") ופועלת <strong>הפוך</strong> ממה ש-{% equation %}Q{% endequation %} אמרה - אם {% equation %}Q{% endequation %} אמרה ש-{% equation %}x{% endequation %} עוצרת על {% equation %}x{% endequation %}, אז {% equation %}U{% endequation %} נכנסת ללולאה אינסופית; ואחרת, {% equation %}U{% endequation %} עוצרת. בבירור ההתנהגות של {% equation %}U{% endequation %} כשיריצו אותה על הקלט {% equation %}U{% endequation %} תהיה פרדוקסלית, וזה סוף הסיפור.

ההוכחה הקצרצרה הזו מתארת אי שוויון בין מחלקות של בעיות חישוביות - במקרה הזה, בין המחלקה {% equation %}\mbox{R}{% endequation %} של בעיות שניתנות לפתרון, ו<a href="http://www.gadial.net/?p=60">המחלקה</a> {% equation %}\mbox{RE}{% endequation %} של בעיות שניתנות לפתרון "חד צדדי"- בעיות שעבורן קיימת מכונה שעוצרת ועונה "כן" אם התשובה היא אכן כן, אך אחרת ייתכן שהיא לא תעצור כלל (או שתעצור ותגיד "לא"). אף שזה לא ברור מייד, שאלת {% equation %}\mbox{P} \ne \mbox{NP}{% endequation %} היא האנלוג הקשור ל"זמן ריצה יעיל" של תוצאת ה-{% equation %}\mbox{R}\ne\mbox{RE}{% endequation %} הזו. (אם לוקחים את הגדרת {% equation %}\mbox{P}{% endequation %} ומחלישים את הדרישה של "זמן ריצה פולינומי" על ידי החלפתה ב"זמן ריצה כלשהו, העיקר שהמכונה תעצור", מקבלים את {% equation %}\mbox{R}{% endequation %}; ואם עושים את אותו הדבר ל-{% equation %}\mbox{NP}{% endequation %} מקבלים את {% equation %}\mbox{RE}{% endequation %} - זה תרגיל נחמד שאולי גם אדבר עליו פעם בבלוג).

ההוכחה הזו מחוכמת למדי - במקום לנסות ולתפוס את כל הדרכים האפשריות שבהן אפשר, אולי, להכריע את בעיית העצירה ולהראות שבכל אחת מהן יש כשל כלשהו, ההוכחה הזו הולכת בדלת האחורית - היא מניחה שאפשר להכריע את בעיית העצירה, ומראה אילו דברים אבסורדיים נובעים מכך. אם כן, מדוע לא ניתן להשתמש בהוכחה הזו גם כדי להראות ש-{% equation %}\mbox{P}{% endequation %} שונה מ-{% equation %}\mbox{NP}{% endequation %}?

הבעיה היא שלא ברור באיזו בעיה כדאי להשתמש בתור הבעיה-חסומת-הזמן שאנלוגית לבעיית העצירה. אפשר להגדיר כל מני שפות דומות אבל אני מעדיף להציג גישה שונה מעט להוכחה שהצגתי לעיל - גישה שבפועל היא שימושית מאוד, ואולי מבהירה מעט יותר טוב מדוע להוכחה הזו קוראים <strong>לכסון</strong>.

הרעיון בהוכחה הוא זה: אם יש לנו שתי מחלקות {% equation %}A,B{% endequation %} של שפות ("שפה"היא פשוט אוסף של קלטים - נניח, אוסף הקלטים שעליהם המכונה עוצרת ואומרת "כן") ואנו רוצים להראות כי {% equation %}A\ne B{% endequation %}, וכמו כן {% equation %}A{% endequation %} בבירור מוכל ב-{% equation %}B{% endequation %}, אז דרך אחת להראות זאת היא על ידי הצגת מכונה ששפתה נמצאת ב-{% equation %}B{% endequation %}, אבל היא מתנהגת באופן שונה מאשר <strong>כל</strong> מכונה ששפתה ב-{% equation %}A{% endequation %}. מה ה"לכסון"כאן? ובכן, זכרו שבהוכחת <a href="http://www.gadial.net/?p=52">האלכסון של קנטור</a> התעלול היה לבנות מספר ממשי ש"מתנהג באופן שונה" מאשר כל מספר ממשי שהיה קיים במספור של הממשיים - כלומר, הוא נבדל מכל אחד מהמספרים הללו באחד מהמקומות בפיתוח העשרוני שלהם. כאן זה אותו רעיון: אם {% equation %}U{% endequation %} היא המכונה שאנו בונים ו-{% equation %}M{% endequation %} היא מכונה כלשהי ששפתה ב-{% equation %}A{% endequation %}, אז יהיה קיים קלט {% equation %}x{% endequation %} שעליו {% equation %}U{% endequation %} ו-{% equation %}M{% endequation %} יתנהגו שונה (ובפרט לכל {% equation %}M{% endequation %} יהיה מדובר על {% equation %}x{% endequation %} אחר).

כאשר {% equation %}A=\mbox{R}{% endequation %} ו-{% equation %}B=\mbox{RE}{% endequation %}, אז המכונות ששפתן ב-{% equation %}A{% endequation %} הן "מכונות שעוצרות תמיד" ואילו מכונות ששפתן ב-{% equation %}B{% endequation %} הן "מכונות שעוצרות תמיד אם התשובה היא "כן", ואחרת יכולות לא לעצור". במילים אחרות, המכונה {% equation %}U{% endequation %} שנבנה יכולה לא לעצור על קלטים מסויימים, ואז מובטח שהם לא יהיו בשפה שלה.

כעת הבניה של {% equation %}U{% endequation %} היא פשוטה ביותר: בהינתן קלט {% equation %}x{% endequation %}, {% equation %}U{% endequation %} <strong>מפרשת</strong> אותו כמכונה {% equation %}M_{x}{% endequation %}, מריצה את {% equation %}M_{x}{% endequation %} על הקלט {% equation %}x{% endequation %} עצמו, ואם {% equation %}M_{x}{% endequation %} עצרה וענתה - היא עונה הפוך ממנה. מכיוון שכל {% equation %}M{% endequation %} ששפתה ב-{% equation %}\mbox{R}{% endequation %} מחוייבת לעצור, מובטח לנו ש-{% equation %}U{% endequation %} תענה הפוך מכל {% equation %}M{% endequation %} כזו על הקלט {% equation %}\left\langle M\right\rangle {% endequation %} עצמו (הסוגריים המשולשים באים לציין שמדובר על <strong>הקידוד</strong> של {% equation %}M{% endequation %} כמחרוזת). כמובן ש-{% equation %}U{% endequation %} עלולה לא לעצור כלל אם המכונה {% equation %}M_{x}{% endequation %} שהיא מסמלצת היא מהסוג שלא עונה אף פעם - אבל זה בסדר, כי הרשינו ל-{% equation %}B{% endequation %} להתנהג כך.

מכיוון שלא ממש ברור איך נראית השפה ש-{% equation %}U{% endequation %} מקבלת, תוצאה זו לא נותנת לנו שפה קונקרטית שלא ניתן להכריע (ועל כן ההוכחה הראשונה שהצגתי עדיפה על פניה באספקט זה) אך היא מראה כי המחלקות {% equation %}\mbox{R}{% endequation %} ו-{% equation %}\mbox{RE}{% endequation %} הן שונות; וחשוב מכך, ניתן להכליל אותה לסיטואציות רבות אחרות. אדגים כעת את אחת מהפשוטות שבהן: נניח שאנו רוצים להוכיח כי {% equation %}\mbox{P} \ne \mbox{R}{% endequation %}, דהיינו שיש בעיות שניתן להכריע אך אינן פתירות בזמן פולינומי - ההוכחה תעבוד כמעט באותו האופן, למעט תוספת טכנית חשובה אחת. אני מזהיר מראש - ההוכחה אינה פשוטה לגמרי וחלקכם כנראה יאבד אותי - אפשר לעבור לסוף ההוכחה בלי לפגוע מהותית בקריאת הפוסט.

שימו לב שכעת {% equation %}U{% endequation %} שלנו צריכה לעצור תמיד, אחרת ייתכן ששפתה לא תשתייך ל-{% equation %}\mbox{R}{% endequation %}. במילים אחרות, תמו ימי הנעורים הפרועים שבהם {% equation %}U{% endequation %} יכלה פשוט להריץ כל מכונת טיורינג עם כל קידוד שהוא, כי ייתכן שחלק מהמכונות שהיא מריצה לא יעצרו לעולם. כאן נכנס לתמונה התעלול הטכני - {% equation %}U{% endequation %} תפרש את הקלט {% equation %}x{% endequation %} כמכונה כמו קודם, אבל תריץ את {% equation %}M_{x}{% endequation %} על {% equation %}x{% endequation %} רק במשך {% equation %}2^{\left|x\right|}{% endequation %} צעדים - שתיים בחזקת האורך של {% equation %}x{% endequation %} צעדים (זכרו - {% equation %}x{% endequation %} היא מחרוזת). אם בפרק הזמן הזה {% equation %}M_{x}{% endequation %} עצרה על {% equation %}x{% endequation %}, הרי ש-{% equation %}U{% endequation %} תענה הפוך ממנה; ואחרת, פשוט תדחה. מה שאנו מתבססים עליו כאן הוא שלכל מכונה יש אינסוף קידודים מאורכים שונים ומשונים, כי תמיד אפשר להכריז שאם תו מסויים מופיע בקידוד פשוט מתעלמים ממנו (למי שזה מפריע לו - יש עוד דרכים, טיפה פחות אלגנטיות, לעקוף את הבעיה הזו).

כעת מגיע החלק המסובך - נניח שיש מכונה {% equation %}M{% endequation %} שפועלת בזמן ריצה פולינומי, נניח עם פולינום {% equation %}p\left(n\right){% endequation %}. אז קיים {% equation %}m{% endequation %} טבעי כלשהו כך ש-{% equation %}p\left(m\right)&lt;2^{m}{% endequation %} - זה מכיוון שפונקציה מעריכית כמו {% equation %}2^{x}{% endequation %} גדלה מהר יותר מכל פולינום (טענה שדורשת הוכחה אך אינה מסובכת). בואו ניקח בתור {% equation %}x{% endequation %} עותק של {% equation %}M{% endequation %} שאורכו לפחות {% equation %}m{% endequation %} - כעת מובטח לנו שכאשר {% equation %}U{% endequation %} תרוץ על {% equation %}x{% endequation %} היא תסמלץ את ריצת {% equation %}M{% endequation %} על {% equation %}x{% endequation %} למשך מספר צעדים כה גדול עד כי מובטח ש-{% equation %}M{% endequation %} תעצור על {% equation %}x{% endequation %}, ולכן {% equation %}U{% endequation %} תענה הפוך מ-{% equation %}M{% endequation %}. מכאן שאף מכונה פולינומית אינה מקבלת את אותה שפה בדיוק כמו {% equation %}U{% endequation %}, וזהו סוף הסיפור.

את ההוכחה הזו ניתן להמשיך ולשכלל, ולקבל את מה שמכונה "משפטי ההיררכייה" של תורת הסיבוכיות. הם מראים, למשל, שיש בעיות שניתן לפתור בסיבוכיות זמן {% equation %}O\left(n^{2}\right){% endequation %} אך לא בסיבוכיות זמן {% equation %}O\left(n\right){% endequation %}, וכדומה. אפשר להחיל את אותו רעיון גם על מחלקות סיבוכיות אי דטרמיניסטיות (הדבר דורש עוד תעלולים לא פשוטים), וישנן עוד הוכחות לכסון מחוכמות אף יותר - המפורסם ביותר מבין התוצאות המחוכמות הוא ככל הנראה <a href="http://en.wikipedia.org/wiki/NP-Intermediate">משפט לדנר</a>, שמראה שאם {% equation %}\mbox{P} \ne \mbox{NP}{% endequation %} אז קיימות "שפות ביניים" שאינן ב-{% equation %}\mbox{P}{% endequation %} וגם אינן {% equation %}\mbox{NP}{% endequation %}-שלמות, אך נעזוב את זה.

הפאנץ' המרכזי בכל הוכחות הלכסון הללו הוא המיעוט בהנחות קונקרטיות שהן דורשות מאיתנו; הרעיון שחוזר שוב ושוב בכולן הוא שאפשר לקודד מכונת טיורינג קידוד סופי, כך שמכונה אחרת יכולה לקרוא את הקידוד הזה ולסמלץ אותה בלי תוספת משאבים משמעותית. זה הכל. הוכחות שמתבססות רק על תכונות אלו מכונות "הוכחות רלטביסטיות". באופן ציורי אפשר לומר שאלו הן הוכחות שמתייחסות למכונת הטיורינג כאל "קופסה שחורה"- אפשר להריץ אותה על קלט מספר כלשהו של צעדים, וזהו. זה כל מה שעושים איתה. אין שום התייחסות לתכונות אחרות של המכונה או לסיטואציות שעשויות לצוץ בזמן הריצה. זו הוכחה מופשטת שכמעט ואינה תלויה בפרטי המודל - והבעיה היא ככל הנראה שהיא מופשטת <strong>מדי</strong>.

האם גם את {% equation %}\mbox{P} \ne \mbox{NP}{% endequation %} ניתן להוכיח בדרך זאת? נסיון נאיבי לעשות זאת ייכשל - היתרון היחיד שיש למכונות ששפתן ב-{% equation %}\mbox{NP}{% endequation %} על פני מכונות ב-{% equation %}\mbox{P}{% endequation %} הוא שהן יכולות להיות אי-דטרמיניסטיות; לא אכנס להגדרה המדוייקת של המושג (שכבר עסקתי בה בעבר) כי זה לא קריטי כרגע - הנקודה היא שעל פניו זה לא מאפשר למכונה לבצע סימולציה "עד הסוף" של כל המכונות הפולינומיות הדטרמיניסטיות; במשפטי הלכסון הקלאסיים הבעיה הזו נפתרת על ידי כך ש-{% equation %}U{% endequation %} רצה <strong>הרבה</strong> זמן ביחס למכונות שהיא מנסה לענות שונה מהן - כאן ל-{% equation %}U{% endequation %} אין שום יתרון כזה.

כמובן שבעיה אינטואיטיבית שכזו לא אמורה לעצור אף אחד. מה שעצר אנשים היה מאמר משנת 1975 של Baker-Gill-Solovay שהראה שפשוט לא ניתן להשתמש בשיטות רלטביסטיות כדי להוכיח ש-{% equation %}\mbox{P} \ne \mbox{NP}{% endequation %}. איך מוכיחים דבר כזה? להוכחה המדוייקת אקדיש פוסט נפרד וכעת אסתפק בתיאור הרעיון. המושג החדש שהם מכניסים לתמונה הוא זה של <a href="http://he.wikipedia.org/wiki/%D7%90%D7%95%D7%A8%D7%A7%D7%9C_%28%D7%9E%D7%93%D7%A2%D7%99_%D7%94%D7%9E%D7%97%D7%A9%D7%91%29">אורקל</a>. אורקל, בפשטות, הוא כוח שמיימי שמסוגל לענות על שאלות מסויימות באופן מושלם ומבלי שהדבר ייקח זמן. באופן קצת יותר פורמלי מדברים תמיד על אורקל לשפות מסויימות. אורקל לשפה יכול, בהינתן מילה כלשהי, לומר מייד אם היא שייכת לשפה או לא. למשל - אורקל לבעיית העצירה יכול, בהינתן זוג {% equation %}M,x{% endequation %}, להגיד מייד אם {% equation %}M{% endequation %} עוצרת על {% equation %}x{% endequation %} או שאינה עוצרת. זהו כמובן מושג תיאורטי לחלוטין; במציאות אפילו חישובים פשוטים דורשים זמן. עם זאת, התועלת שצומחת משימוש תיאורטי ביצור הזה היא עצומה, והדבר דומה לשימושיות הרבה של מושג המכונה האי-דטרמיניסטית, למרות שמכונה כזו אינה קיימת במציאות.

כעת, בהינתן מודל כלשהו של מכונות טיורינג (למשל - מכונות דטרמיניסטיות פולינומיות) אפשר "לחזק" את המודל על ידי כך שמרשים למכונות בו גישה לאורקל מסויים (כלומר, אורקל עבור שפה ספציפית נתונה). למשל, את המודל של "מכונות דטרמיניסטיות פולינומיות"אפשר לחזק ולהפוך למודל של "מכונות דטרמיניסטיות פולינומיות עם אורקל לבעיית העצירה".

אלא מה? הוכחות רלטיביסטיות הן "עיוורות" לחיזוק שכזה. אם אנחנו מצליחים להוכיח באופן רלטיביסטי ששתי מחלקות {% equation %}A,B{% endequation %} שונות זו מזו, ואנו מחזקים את המכונות <strong>בשתי</strong> המחלקות באמצעות אותו אורקל, ההוכחה ממשיכה לעבוד באותו האופן; בכל פעם שסימולציה של מכונה {% equation %}M{% endequation %} מתוך {% equation %}A{% endequation %} תדרוש קריאה לאורקל, {% equation %}U{% endequation %} תוכל לבצע את הקריאה הזו כי גם ל-{% equation %}B{% endequation %} הוספנו גישה לאותו אורקל. באופן פורמלי זה אומר שאם הוכחנו רלטיביסטית ש-{% equation %}A\ne B{% endequation %} אז גם {% equation %}A^{L}\ne B^{L}{% endequation %}, כאשר {% equation %}A^{L}{% endequation %} אומר, כצפוי, "המחלקה {% equation %}A{% endequation %} כשמוסיפים למכונות בה גישה לאורקל לשפה {% equation %}L{% endequation %}".

ומה שהראו באותו מאמר משנת 1975 היה שקיימות שתי שפות, {% equation %}L_{1},L_{2}{% endequation %}, כך ש-{% equation %}\mbox{P}^{L_{1}}\ne\mbox{NP}^{L_{1}}{% endequation %}, אבל {% equation %}\mbox{P}^{L_{2}}=\mbox{NP}^{L_{2}}{% endequation %}. זה מראה מייד שלא ניתן להוכיח לא ש-{% equation %}\mbox{P}\ne\mbox{NP}{% endequation %} בשיטות רלטביסטיות, וגם לא ש-{% equation %}\mbox{P}=\mbox{NP}{% endequation %}.

מהן השפות {% equation %}L_{1},L_{2}{% endequation %} המסתוריות הללו ואיך הולכת ההוכחה? מכיוון שהיא טכנית יחסית, אדחה אותה לפוסט נפרד.